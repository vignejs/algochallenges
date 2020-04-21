#include "sum_of_multiples.h"
#include <algorithm>

namespace sum_of_multiples {

    int to(const std::vector<int> &arr, int i) {
        int sum = 0;
        for (--i; i >= 1; --i) {
            std::find_if(arr.begin(), arr.end(), [&](const int &a) {
                if (i % a == 0) {
                    sum += i;
                    return true;
                } else{
                    return false;
                }
            });
        }
        return sum;
    }

}  // namespace sum_of_multiples
