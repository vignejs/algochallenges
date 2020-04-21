#if !defined(PHONE_NUMBER_H)
#define PHONE_NUMBER_H
#include <string>
#include <utility>
#include <algorithm>
#include <initializer_list>
namespace phone_number {

    struct phone_number {
    private:

    public:
        std::string no;
        explicit phone_number (std::string);
        std::string number();
        std::string area_code();
        explicit operator std::string () const {
            return "SomeClassStringRepresentation";
        }
    };


}  // namespace phone_number

#endif // PHONE_NUMBER_H
