#include "nucleotide_count.h"


namespace nucleotide_count {

    std::map<char, int> counter::nucleotide_counts() const {
        std::map<char, int> seqcount{{'A', 0},
                                     {'T', 0},
                                     {'C', 0},
                                     {'G', 0}};
        std::for_each(dnaseq.begin(), dnaseq.end(), [&](char const &c) {
            seqcount[c] += 1;
        });

        return seqcount;
    }

    int counter::count(char curr) const {
        int total = 0;
        std::for_each(dnaseq.begin(), dnaseq.end(), [&](char const &c) {
            if (possibilites.find(curr) == std::string::npos) {
                throw std::invalid_argument("illegal char");
            }
            if (c == curr) {
                total += 1;
            }
        });
        return total;
    }
}  // namespace nucleotide_count
