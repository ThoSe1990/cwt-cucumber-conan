

cmake_minimum_required(VERSION 3.16)
project(cwt-cucumber VERSION 1.0.0)

set(CMAKE_CXX_STANDARD 17)

if (NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Debug)
endif()

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

set(target box)

find_package(cwt-cucumber REQUIRED)

add_executable(${target} 
  ${CMAKE_CURRENT_SOURCE_DIR}/step_definition/step_definition.cpp
)
target_include_directories(${target} PRIVATE ${PROJECT_SOURCE_DIR}/src)
target_link_libraries(${target} cwt::cucumber)