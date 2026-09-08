#pragma once
#include <stdint.h>
#include <string.h>

namespace audio {
constexpr uint32_t sampleRate = 16000;
constexpr uint32_t chunkBytes = sampleRate * 2 * 15;
inline void le32(uint8_t* out, uint32_t n) {
  for (unsigned i = 0; i < 4; ++i) out[i] = uint8_t(n >> (8*i));
}
inline void wavHeader(uint8_t* h, uint32_t bytes) {
  memset(h, 0, 44);
  memcpy(h, "RIFF", 4); le32(h+4, bytes+36);
  memcpy(h+8, "WAVEfmt ", 8); le32(h+16, 16);
  h[20]=1; h[22]=1; le32(h+24, sampleRate);
  le32(h+28, sampleRate*2); h[32]=2; h[34]=16;
  memcpy(h+36, "data", 4); le32(h+40, bytes);
}
inline uint32_t crc32(const uint8_t* p, unsigned n) {
  uint32_t c = 0xffffffffU;
  while (n--) {
    c ^= *p++;
    for (unsigned i=0; i<8; ++i) c=(c>>1) ^ (0xedb88320U & (0U-(c&1)));
  }
  return ~c;
}
}