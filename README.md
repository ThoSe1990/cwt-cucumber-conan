The Conan recipe and the examples from this GitHub repository refer to [CWT-Cucumber: A simple C/C++ Cucumber Interpreter](https://github.com/ThoSe1990/cwt-cucumber).

  
# CWT-Cucumber: Conan Recipe

At the moment, the Conan recipe is not pushed to the conancenter. For now, I maintain the recipe in this repo, to build the package locally and to use cwt-cucumber. In the long run, I'll consider moving the recipe to conancenter.

## CMake Integration

When you integrate this into your projects, there is not too much to do: 

- Find the cwt-cucumber package: `find_package(cucumber REQUIRED)`
- Compile your sources / steps
- Link against `cucumber::cucumber` or `cucumber::cucumber-no-main`

## Build the Conan Package & Examples

Move to `./package` and create the conan package:

```shell
cd package
conan create . --version 1.1.0 --user cwt --channel stable
```

If you want to use another user and channel, feel free to do so. But remember to use them correctly in the consumer's `conanfile.txt`
  
And now you can move over to `./consumer` to build the examples: 

```
cd ../consumer
conan install . -of ./build 
cmake -S . -B ./build -DCMAKE_TOOLCHAIN_FILE=./build/conan_toolchain.cmake 
cmake --build ./build
```

And now you can execute the feature files, for example:

```
./build/bin/Debug/box ./features/1_first_scenario.feature

Feature: My first feature  ./features/1_first_scenario.feature:2

Scenario: First Scenario  ./features/1_first_scenario.feature:5
[   PASSED    ] An empty box  ./features/1_first_scenario.feature:6
[   PASSED    ] I place 2 x "apple" in it  ./features/1_first_scenario.feature:7
[   PASSED    ] The box contains 2 item(s)  ./features/1_first_scenario.feature:8


1 Scenarios (1 passed)
3 Steps (3 passed)
```
