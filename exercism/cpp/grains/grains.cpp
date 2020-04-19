#include "grains.h"

namespace grains {

    unsigned long long square(const int &x) {
        return pow(2, x-1);
    }

    unsigned long long total() {
        unsigned long long t = square(64);
        for (int i = 1; i <= 64; i++){
            t += t / 2;
        }
        return t;
    }
}  // namespace grains
