#if !defined(GIGASECOND_H)
#define GIGASECOND_H

#include "boost/date_time/posix_time/posix_time.hpp"
using namespace boost::posix_time;

namespace gigasecond {

    const ptime advance(boost::posix_time::ptime ptime);


}  // namespace gigasecond

#endif // GIGASECOND_H
