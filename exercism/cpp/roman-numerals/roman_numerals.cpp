#include "roman_numerals.h"

namespace roman_numerals {

    std::string repeat(const std::string &input, size_t num) {
        std::ostringstream os;
        std::fill_n(std::ostream_iterator<std::string>(os), num, input);
        return os.str();
    }

    std::string convert(int number) {
        std::string result;
        std::find_if(roman.rbegin(), roman.rend(), [&](const std::pair<int, std::string> &element) {
            int key = element.first;
            int x = number / key;
            result.append(repeat(element.second, x));
            number -= key * x;
            return number <= 0;
        });
        return result;
    }
}  // namespace roman_numerals
