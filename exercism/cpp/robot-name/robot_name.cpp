#include "robot_name.h"

namespace robot_name {

    std::string robot::gen_id() {
        std::random_device rd;
        std::mt19937 mt(rd());
        std::uniform_int_distribution<int> alpha('A', 'Z'), numeric('0', '9');
        std::string unique_id;
        std::size_t size = 2;
        std::generate_n(std::back_inserter(unique_id), size, [&] { return alpha(mt); });
        size = 3;
        std::generate_n(std::back_inserter(unique_id), size, [&] { return numeric(mt); });
        return unique_id;
    }

    std::string robot::name() const {
        return result;
    }

    void robot::reset() {
        result = gen_id();
    }

}  // namespace robot_name
