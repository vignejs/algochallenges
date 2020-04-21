#include "grains.h"

namespace grains {

    ull square(int y) {
        return 1ull << (y - 1);
    }

    ull total() {
        return std::bitset<64>().set().to_ulong();
    }
}  // namespace grains
