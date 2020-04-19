#if !defined(TRIANGLE_H)
#define TRIANGLE_H
#include <array>
#include <algorithm>
#include <stdexcept>

namespace triangle {

    enum class flavor {
        equilateral,
        isosceles,
        scalene,
        degenerate,
    };

    flavor kind(double, double, double);

}  // namespace triangle

#endif // TRIANGLE_H
