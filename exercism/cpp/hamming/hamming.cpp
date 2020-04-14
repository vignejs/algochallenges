#include "hamming.h"
#include <string>
#include <iostream>
#include <stdexcept>
namespace hamming {
    int compute(std::string str1, std::string str2) {
        if (str1.size() != str2.size()) throw std::domain_error("unequal strings");
        int d = 0;
        for (std::string::size_type i = 0; i < str1.size(); i++) {
            if (str1[i] != str2[i]){
                d++;
            }
            else continue;
        }
        return d;
    }
}  // namespace hamming
