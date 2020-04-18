#include "triangle.h"

namespace triangle {
    int kind(float x, float y, float z) {
        if (x + y < z || y + z < x || x + z < y || x <= 0 || y <= 0 || z <= 0) {
            throw std::domain_error("illegal triangle");
        } else {
            if (x == y && y == z && x == z) {
                return 0;
            } else if (x + y == z || y + z == x || x + z == y) {
                return 3;
            } else if (x == y || y == z || x == z) {
                return 1;
            } else {
                return 2;
            }
        }
    }
}
