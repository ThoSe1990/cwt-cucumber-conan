#include <iostream>

#include "cwt/cucumber.hpp"

int main(int argc, const char* argv[])
{
  std::cout << "----------------------------------------\n";
  std::cout << "Executing cwt-cucumber from our own main\n";
  std::cout << "----------------------------------------\n";

  cuke::details::init(); 
  int result = cuke::details::run(argc, argv);

  std::cout << "----------------------------------------\n";
  std::cout << "This was executed by our own main!\n";

  return result;
}