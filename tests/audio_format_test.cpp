#include "audio_format.h"
#include <assert.h>
#include <initializer_list>
static uint32_t read32(const uint8_t* p) {
  return uint32_t(p[0]) | uint32_t(p[1])<<8 | uint32_t(p[2])<<16 | uint32_t(p[3])<<24;
}
int main() {
  uint8_t h[44];
  for (uint32_t n : {0U, 2U, 480000U}) {
    audio::wavHeader(h,n);
    assert(read32(h+4)==n+36 && read32(h+40)==n);
    assert(read32(h+24)==16000 && read32(h+28)==32000);
    assert(h[20]==1 && h[22]==1 && h[32]==2 && h[34]==16);
  }
  assert(audio::crc32((const uint8_t*)"123456789",9)==0xcbf43926U);
  assert(audio::chunkBytes==480000);
}