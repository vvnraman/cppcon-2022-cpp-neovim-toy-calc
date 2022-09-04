// Project includes
#include <toddlermath_adder.h>
#include <toddlermath_subtracter.h>

// Standard includes
#include <stdexcept>
#include <vector>

// Third-party includes
#include <CLI/CLI.hpp>
#include <fmt/core.h>
#include <fmt/printf.h>

namespace {  // anonymous

void add_number_options(CLI::App& app, double& num1, double& num2);

}  // namespace

int main(int argc, char const* argv[])
{
  CLI::App app {"A toy calculator program to demo Neovim on the command line",
                "calc"};
  try {
    auto* add_child_app_p = app.add_subcommand("add", "Add 2 numbers");
    auto* sub_child_app_p = app.add_subcommand("sub", "Subtract 2 numbers");

    double num1 {};
    double num2 {};
    add_number_options(*add_child_app_p, num1, num2);
    add_number_options(*sub_child_app_p, num1, num2);

    app.require_subcommand(1);

    app.parse(argc, argv);

    if (app.got_subcommand("add")) {
      vvnraman::toddlermath::Adder adder({num1, num2});
      auto result = adder.run();
      fmt::print("{} + {} = {}\n", num1, num2, result);

    } else if (app.got_subcommand("sub")) {
      vvnraman::toddlermath::Subtracter subtracter(num1, num2);
      auto result = subtracter.run();
      fmt::print("{} - {} = {}\n", num1, num2, result);
    }

  } catch (const CLI::ParseError& pe) {
    return app.exit(pe);
  } catch (const std::runtime_error& re) {
    fmt::print(stderr, "runtime_error: {}", re.what());
    return -1;
  }
  return 0;
}

namespace {  // anonymous

void add_number_options(CLI::App& app, double& num1, double& num2)
{
  app.add_option("num1", num1, "First number");
  app.add_option("num2", num2, "Second number");
}

}  // namespace
