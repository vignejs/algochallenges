#include "grade_school.h"

namespace grade_school {

    map<int, vector<string>> school::roster() const {
        return _roster;
    }

    vector<string> school::grade(int grade) const {
        try {
            return _roster.at(grade);
        } catch (out_of_range &) {
            return vector<string>();
        }
    }

    void school::add(const string& name, int grade) {
        _roster[grade].insert(_roster[grade].begin(), name);
        vector<string> names = _roster.at(grade);
        sort(names.begin(), names.end());
        _roster[grade] = names;
    }
}  // namespace grade_school
