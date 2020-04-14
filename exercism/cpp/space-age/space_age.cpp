#include "space_age.h"

namespace space_age {

    double space_age::seconds() const {
        return sec;
    }

    constexpr double space_age::on_mercury() {
        return earth_years / 0.2408467;
    }

    constexpr double space_age::on_venus() {
        return earth_years / 0.61519726;
    }

    constexpr double space_age::on_earth() {
        return earth_years;
    }

    constexpr double space_age::on_mars() {
        return earth_years / 1.8808158;
    }

    constexpr double space_age::on_jupiter() {
        return earth_years / 11.862615;
    }

    constexpr double space_age::on_saturn() {
        return earth_years / 29.447498;
    }

    constexpr double space_age::on_uranus() {
        return earth_years / 84.016846;
    }

    constexpr double space_age::on_neptune() {
        return earth_years / 164.79132;
    }
}  // namespace space_age
