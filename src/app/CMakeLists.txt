add_executable(calc app_main.cpp)

find_package(fmt REQUIRED)
find_package(scn CONFIG REQUIRED)
find_package(CLI11 CONFIG REQUIRED)

target_link_libraries(calc PRIVATE
  toddlermath
  fmt::fmt
  scn::scn
  CLI11::CLI11)

install(TARGETS calc)
