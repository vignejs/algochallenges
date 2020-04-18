#if !defined(NUCLEOTIDE_COUNT_H)
#define NUCLEOTIDE_COUNT_H

#include <string>
#include <map>
#include <utility>
#include <algorithm>

namespace nucleotide_count {
    struct counter {
    private:
        std::string dnaseq;
        std::string possibilites = "ATCG";
    public:
        explicit counter(std::string dna) :
                dnaseq(std::move(dna)) {
            std::for_each(dnaseq.begin(), dnaseq.end(), [&](char const &c) {
                if (possibilites.find(c) == std::string::npos) {
                    throw std::invalid_argument("illegal char");
                }
            });
        }

        std::map<char, int> nucleotide_counts() const;

        int count(char) const;
    };

}  // namespace nucleotide_count

#endif // NUCLEOTIDE_COUNT_H
