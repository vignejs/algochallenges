#include "difference_of_squares.h"
#include <cmath>
#include <iostream>

namespace difference_of_squares {

    int square_of_sum(int x) {
        int sum = 0;
        for (; x > 0; x--) {
            sum += x;
        }

        return pow(sum, 2);
    }

    int sum_of_squares(int x) {
        int sum = 0;
        for (; x > 0; x--) {
            sum += pow(x, 2);
        }
        return sum;
    }

    int difference(int x) {
        return square_of_sum(x) - sum_of_squares(x);
    }
}  // namespace difference_of_squares

