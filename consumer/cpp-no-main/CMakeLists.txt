
set(target box-no-main)

add_executable(${target}
${CMAKE_CURRENT_SOURCE_DIR}/step_definition/step_definition.cpp
${CMAKE_CURRENT_SOURCE_DIR}/step_definition/main.cpp
)
target_link_libraries(${target} cwt::cucumber-no-main)