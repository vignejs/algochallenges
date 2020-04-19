#if !defined(GRADE_SCHOOL_H)
#define GRADE_SCHOOL_H
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

namespace grade_school {
    struct school {
    private:
        map<int, vector<string>> _roster;
    public:
        school () : _roster() {}
        map<int, vector<string>> roster() const;
        vector<string> grade(int) const;
        void add(const string&, int);
    };

}  // namespace grade_school

#endif // GRADE_SCHOOL_H
