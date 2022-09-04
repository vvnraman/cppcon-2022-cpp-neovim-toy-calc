#pragma once

namespace vvnraman {
namespace toddlermath {

// @brief Encapsulates the logic to subtract 2 numbers
class Subtracter
{
public:
  explicit Subtracter(double num1, double num2);

  // @brief Executes the subtraction operation and returns the result
  double run();

private:
  double m_num1;
  double m_num2;
};

}  // namespace toddlermath
}  // namespace vvnraman
