#include "reverse_string.h"
#include <string>
#include <algorithm>
namespace reverse_string {
    std::string reverse_string1(std::string s) {
        std::reverse(std::begin(s), std::end(s));
        return s;
    }
    std::string reverse_string(std::string input) {
        std::string output(input.rbegin(), input.rend());
        return output;
    }
}  // namespace reverse_string
