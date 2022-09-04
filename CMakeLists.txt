cmake_minimum_required(VERSION 3.24)
project(toy-calculator CXX)

# DO NOT DO THIS IN YOUR CMakeLists.txt. THIS SHOULD BE SET IN YOUR TOOLCHAIN
# FILE. THIS DEMO PROJECT IS PRIMARILY FOR NEOVIM DEMO HENCE THIS IS NON CMAKE
# DEMOWARE AND HENCE JUSTIFIED.
set(CMAKE_CXX_STANDARD 20 CACHE STRING "C++ standard to be used")

enable_testing()

add_subdirectory(src)
add_subdirectory(tests)
