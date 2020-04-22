#include "pangram.h"

namespace pangram {

    bool is_pangram(const std::string& sent) {
        std::bitset<26> azbits;
        azbits.set();
        std::for_each(sent.begin(), sent.end(), [&](const char &c){
            if (std::isalpha(c)){
                azbits[std::tolower(c) - 'a'] = false;
            }
        });
        return azbits == 0;
    }
}  // namespace pangram
