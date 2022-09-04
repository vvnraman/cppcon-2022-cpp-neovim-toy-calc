add_library(toddlermath
  toddlermath_add.cpp
  toddlermath_subtract.cpp
  toddlermath_adder.cpp
  toddlermath_subtracter.cpp)

target_include_directories(toddlermath
  PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}")
