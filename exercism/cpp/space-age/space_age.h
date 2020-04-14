#if !defined(SPACE_AGE_H)
#define SPACE_AGE_H

namespace space_age {
    struct space_age{
    private:
        double sec;
        double earth_years;
    public:
        explicit space_age(double space_sec){
            sec = space_sec;
            earth_years = sec / 31557600;
        }
        double seconds() const;
        constexpr double on_mercury();
        constexpr double on_venus();
        constexpr double on_earth();
        constexpr double on_mars();
        constexpr double on_jupiter();
        constexpr double on_saturn();
        constexpr double on_neptune();
        constexpr double on_uranus();
    };
}  // namespace space_age

#endif // SPACE_AGE_H
