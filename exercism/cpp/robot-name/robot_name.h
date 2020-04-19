#if !defined(ROBOT_NAME_H)
#define ROBOT_NAME_H

#include <string>
#include <random>
#include <algorithm>

// get base random alias which is auto seeded and has static API and internal state

namespace robot_name {

    struct robot {
    private:
        std::string result;
    public:
        static std::string gen_id();

        robot() : result(gen_id()) {}

        std::string name() const;

        void reset();
    };

}  // namespace robot_name

#endif // ROBOT_NAME_H
