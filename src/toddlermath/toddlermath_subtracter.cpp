// Project includes
#include <toddlermath_subtracter.h>
#include <toddlermath_subtract.h>

namespace vvnraman {
namespace toddlermath {

Subtracter::Subtracter(double num1, double num2)
    : m_num1(num1)
    , m_num2(num2)
{
  // Empty body
}

double Subtracter::run()
{
  return subtract(m_num1, m_num2);
}

}  // namespace toddlermath
}  // namespace vvnraman
