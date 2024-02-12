

cmake_minimum_required(VERSION 3.16)
project(cucumber-conan-example VERSION 1.0.0)

set(CMAKE_CXX_STANDARD 20)

# if (NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Debug)
# endif()

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

if(MSVC)
    add_compile_options(
        $<$<CONFIG:>:/MT> 
        $<$<CONFIG:Debug>:/MTd>
        $<$<CONFIG:Release>:/MT>
    )
endif()

find_package(cucumber REQUIRED)

set(target box)

add_executable(${target}
  ${CMAKE_CURRENT_SOURCE_DIR}/step_definition/step_definition.cpp
  ${CMAKE_CURRENT_SOURCE_DIR}/step_definition/hooks.cpp
)

target_link_libraries(${target} cucumber::cucumber)