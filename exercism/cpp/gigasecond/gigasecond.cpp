#include "gigasecond.h"

namespace gigasecond {
    const ptime advance(boost::posix_time::ptime ptime) {
        return ptime + seconds(1000000000);
    }

}  // namespace gigasecond
