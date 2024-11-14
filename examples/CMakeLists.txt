

cmake_minimum_required(VERSION 3.16)
project(cucumber-conan-example)

set(CMAKE_CXX_STANDARD 20)


set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

find_package(cwt-cucumber REQUIRED)

set(target example)

add_executable(${target}
  ${CMAKE_CURRENT_SOURCE_DIR}/step_definition/step_definition.cpp
  ${CMAKE_CURRENT_SOURCE_DIR}/step_definition/hooks.cpp
)

target_link_libraries(${target} cwt::cucumber)
