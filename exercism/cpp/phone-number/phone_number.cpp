#include "phone_number.h"

namespace phone_number {

    phone_number::phone_number (std::string no) :
    no(std::move(no)) {};

    std::string phone_number::number() {
        std::string result;
        std::for_each(no.begin(), no.end(), [&](const char &c){
            if(std::isdigit(c)){
                result += c;
            }
        });
        return result;
    }

    std::string phone_number::area_code() {
        return std::string();
    }

}  // namespace phone_number
