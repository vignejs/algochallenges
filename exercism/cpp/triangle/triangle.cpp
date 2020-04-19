#include "triangle.h"

namespace triangle {
    flavor kind(double x, double y, double z) {
        std::array<double, 3> side{x, y, z};
        std::sort(std::begin(side), std::end(side));
        if (side[0] + side[1] < side[2] || side[0] <= 0) {
            throw std::domain_error("illegal triangle");
        } else if (side[0] == side[2]) {
            return flavor::equilateral;
        } else if (side[0] + side[1] == side[2]) {
            return flavor::degenerate;
        } else if (side[0] == side[1] || side[1] == side[2]) {
            return flavor::isosceles;
        } else {
            return flavor::scalene;
        }
    }
}
