// Project includes
#include <toddlermath_adder.h>
#include <toddlermath_add.h>

namespace vvnraman {
namespace toddlermath {

Adder::Adder(const std::vector<double>& nums)
    : m_nums(nums)
{
  // Empty body
}

double Adder::run()
{
  return add(m_nums);
}

}  // namespace toddlermath
}  // namespace vvnraman
