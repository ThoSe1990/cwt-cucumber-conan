

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

find_package(cwt-cucumber REQUIRED)

add_subdirectory(${CMAKE_SOURCE_DIR}/c)
add_subdirectory(${CMAKE_SOURCE_DIR}/cpp)
add_subdirectory(${CMAKE_SOURCE_DIR}/cpp-no-main)