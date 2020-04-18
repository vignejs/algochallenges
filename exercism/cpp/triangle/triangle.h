#if !defined(TRIANGLE_H)
#define TRIANGLE_H

#include <stdexcept>

namespace triangle {

    enum flavor {
        equilateral,
        isosceles,
        scalene,
        degenerate,
    };

    int kind(float, float, float);

}  // namespace triangle

#endif // TRIANGLE_H
