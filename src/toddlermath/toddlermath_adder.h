#pragma once

// Standard includes
#include <vector>

namespace vvnraman {
namespace toddlermath {

// @brief Encapsulates the logic to add 2 numbers
class Adder
{
public:
  explicit Adder(const std::vector<double>& nums);

  // @brief Executes the add operation and returns the result
  double run();

private:
  const std::vector<double> m_nums;
};

}  // namespace toddlermath
}  // namespace vvnraman
