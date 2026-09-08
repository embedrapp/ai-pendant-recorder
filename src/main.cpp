#include <Arduino.h>
#include <SD.h>
#include <SPI.h>
#include <Preferences.h>
#include "driver/i2s.h"
#include "audio_format.h"

namespace {
constexpr int recordButton=2, micClock=42, micData=41, ampEnable=5;
// Sense expansion: verify CS=21 against the purchased hardware revision.
constexpr int sdCS=21, sdSCK=7, sdMISO=8, sdMOSI=9;
struct Block { uint16_t size; uint8_t data[1024]; };
QueueHandle_t blocks;
EventGroupHandle_t events;
constexpr EventBits_t RUN=1, FAULT=2, ACTIVE=4;
Preferences prefs;
File chunk;
String tempPath;
uint32_t dataBytes=0;

bool writeHeader(File& f, uint32_t bytes) {
  uint8_t h[44]; audio::wavHeader(h,bytes);
  return f.seek(0) && f.write(h,sizeof(h))==sizeof(h);
}

bool finishChunk() {
  if (!chunk) return true;
  bool ok=writeHeader(chunk,dataBytes);
  chunk.flush(); chunk.close();
  if (!ok) return false;
  String finalPath=tempPath.substring(0,tempPath.length()-5)+".wav";
  if (SD.exists(finalPath) || !SD.rename(tempPath,finalPath)) return false;
  Serial.printf("recording:finalized:%s:%lu\n",finalPath.c_str(),(unsigned long)dataBytes);
  return true;
}

bool openChunk() {
  if (SD.totalBytes() <= SD.usedBytes()+audio::chunkBytes+1024*1024) return false;
  // Reserve identity durably before creating the file. Never append after reboot.
  uint32_t id=prefs.getUInt("sequence",0);
  do {
    if (id==UINT32_MAX) return false;
    ++id;
    char name[40]; snprintf(name,sizeof(name),"/audio/%010lu.part",(unsigned long)id);
    tempPath=name;
  } while (SD.exists(tempPath) || SD.exists(tempPath.substring(0,tempPath.length()-5)+".wav"));
  if (prefs.putUInt("sequence",id)!=sizeof(id)) return false;
  chunk=SD.open(tempPath,FILE_WRITE);
  dataBytes=0;
  if (!chunk) return false;
  if (!writeHeader(chunk,0)) { chunk.close(); return false; }
  return true;
}

bool recover() {
  File dir=SD.open("/audio");
  if (!dir || !dir.isDirectory()) return false;
  // Recovery runs before recording tasks; rename only after the iterator closes.
  for (;;) {
    String candidate;
    File f=dir.openNextFile();
    while (f) {
      String n=f.name();
      if (!f.isDirectory() && n.endsWith(".part")) {
        candidate=n.startsWith("/") ? n : String("/audio/")+n;
        f.close(); break;
      }
      f.close(); f=dir.openNextFile();
    }
    dir.close();
    if (!candidate.length()) return true;
    File partial=SD.open(candidate,"r+");
    if (!partial || partial.size()<44) {
      if (partial) partial.close();
      // Keep damaged bytes for service; do not delete unsynced data.
      if (!SD.rename(candidate,candidate+".bad")) return false;
    } else {
      uint32_t bytes=(partial.size()-44)&~1U;
      bool ok=writeHeader(partial,bytes);
      partial.flush(); partial.close();
      String finalPath=candidate.substring(0,candidate.length()-5)+".wav";
      if (!ok || SD.exists(finalPath) || !SD.rename(candidate,finalPath)) return false;
      Serial.printf("recording:recovered:%s\n",finalPath.c_str());
    }
    dir=SD.open("/audio");
    if (!dir) return false;
  }
}

bool initMic() {
  i2s_config_t c={};
  c.mode=(i2s_mode_t)(I2S_MODE_MASTER|I2S_MODE_RX|I2S_MODE_PDM);
  c.sample_rate=audio::sampleRate; c.bits_per_sample=I2S_BITS_PER_SAMPLE_16BIT;
  c.channel_format=I2S_CHANNEL_FMT_ONLY_LEFT;
  c.communication_format=I2S_COMM_FORMAT_STAND_I2S;
  c.intr_alloc_flags=ESP_INTR_FLAG_LEVEL1; c.dma_buf_count=16; c.dma_buf_len=256;
  i2s_pin_config_t p={};
  p.mck_io_num=I2S_PIN_NO_CHANGE; p.bck_io_num=I2S_PIN_NO_CHANGE;
  p.ws_io_num=micClock; p.data_out_num=I2S_PIN_NO_CHANGE; p.data_in_num=micData;
  if (i2s_driver_install(I2S_NUM_0,&c,0,nullptr)!=ESP_OK) return false;
  if (i2s_set_pin(I2S_NUM_0,&p)==ESP_OK) return true;
  i2s_driver_uninstall(I2S_NUM_0); return false;
}

void acquire(void*) {
  Block b;
  for (;;) {
    // Keep draining DMA while idle, avoiding stale audio at start.
    size_t count=0;
    esp_err_t result=i2s_read(I2S_NUM_0,b.data,sizeof(b.data),&count,pdMS_TO_TICKS(100));
    if (result!=ESP_OK) { xEventGroupSetBits(events,FAULT); continue; }
    xEventGroupSetBits(events,ACTIVE);
    if (!(xEventGroupGetBits(events)&RUN)) { xEventGroupClearBits(events,ACTIVE); continue; }
    b.size=count & ~size_t(1);
    if (b.size && xQueueSend(blocks,&b,0)!=pdTRUE) xEventGroupSetBits(events,FAULT);
    xEventGroupClearBits(events,ACTIVE);
  }
}

void writer(void*) {
  Block b;
  bool lastRaw=false, pressed=false, recording=false, healthy=true;
  uint32_t changed=0;
  for (;;) {
    bool raw=digitalRead(recordButton)==LOW;
    if (raw!=lastRaw) { changed=millis(); lastRaw=raw; }
    if (raw!=pressed && millis()-changed>=35) {
      pressed=raw;
      if (pressed && healthy) {
        if (!recording && !chunk && uxQueueMessagesWaiting(blocks)==0 &&
            !(xEventGroupGetBits(events)&ACTIVE)) {
          if (openChunk()) { recording=true; xEventGroupSetBits(events,RUN); }
          else { healthy=false; Serial.println("recording:fault:open-or-full"); }
        } else if (recording) { recording=false; xEventGroupClearBits(events,RUN); }
      }
    }
    if (xEventGroupGetBits(events)&FAULT) {
      recording=false; healthy=false; xEventGroupClearBits(events,RUN);
    }
    if (xQueueReceive(blocks,&b,pdMS_TO_TICKS(5))==pdTRUE && healthy) {
      if (!chunk) healthy=openChunk();
      size_t offset=0;
      while (offset<b.size && healthy) {
        size_t n=min(size_t(b.size-offset),size_t(audio::chunkBytes-dataBytes));
        if (chunk.write(b.data+offset,n)!=n) { healthy=false; break; }
        dataBytes+=n; offset+=n;
        if (dataBytes==audio::chunkBytes) {
          healthy=finishChunk();
          if (healthy && (recording || offset<b.size)) healthy=openChunk();
        }
      }
    }
    if (!healthy) {
      recording=false; xEventGroupClearBits(events,RUN);
      if (chunk) { chunk.flush(); chunk.close(); } // preserve .part for recovery
      xQueueReset(blocks);
    } else if (!recording && !(xEventGroupGetBits(events)&ACTIVE) && uxQueueMessagesWaiting(blocks)==0) {
      healthy=finishChunk();
    }
    if (!healthy) { digitalWrite(ampEnable,LOW); vTaskDelay(pdMS_TO_TICKS(100)); }
  }
}
}

void setup() {
  Serial.begin(115200);
  pinMode(recordButton,INPUT_PULLUP);
  pinMode(ampEnable,OUTPUT); digitalWrite(ampEnable,LOW);
  // No camera initialization, Wi-Fi connection, upload or automatic deletion.
  SPI.begin(sdSCK,sdMISO,sdMOSI,sdCS);
  if (!prefs.begin("recorder",false) || !SD.begin(sdCS,SPI,10000000) ||
      (!SD.exists("/audio") && !SD.mkdir("/audio")) || !recover()) {
    Serial.println("startup:fault:storage"); return;
  }
  blocks=xQueueCreate(32,sizeof(Block)); events=xEventGroupCreate();
  if (!blocks || !events || !initMic()) { Serial.println("startup:fault:audio-memory"); return; }
  TaskHandle_t acquisition=nullptr;
  if (xTaskCreatePinnedToCore(acquire,"capture",4096,nullptr,3,&acquisition,1)!=pdPASS) {
    Serial.println("startup:fault:capture-task"); return;
  }
  if (xTaskCreatePinnedToCore(writer,"storage",8192,nullptr,2,nullptr,0)!=pdPASS) {
    vTaskDelete(acquisition); Serial.println("startup:fault:storage-task"); return;
  }
  Serial.println("ready:press-to-toggle;sync-not-implemented");
}
void loop() { vTaskDelay(pdMS_TO_TICKS(1000)); }
