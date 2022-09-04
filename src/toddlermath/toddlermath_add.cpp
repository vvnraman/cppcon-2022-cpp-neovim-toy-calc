// Project includes
#include <toddlermath_add.h>

// Standard includes
#include <algorithm>
#include <numeric>

namespace vvnraman {
namespace toddlermath {

double add(const std::vector<double> &nums)
{
  // Use standard algorithm to compute the sum
  return std::accumulate(nums.begin(), nums.end(), 0.0);
}

}  // namespace toddlermath
}  // namespace vvnraman
