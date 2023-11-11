Find cwt-cucumber in [this GitHub repository](https://github.com/ThoSe1990/cwt-cucumber)

# CWT-Cucumber: Conan Recipe

At the moment, the Conan recipe is not pushed to the conancenter. For now, I maintain the recipe in this repo, to build the package locally and to use cwt-cucumber. In the long run, I'll consider moving the recipe to conancenter.

## CMake Integration

When you integrate this into your projects, there is not too much to do: 

- Find the cwt-cucumber package: `find_package(cwt-cucumber REQUIRED)`
- Compile your sources / steps
- Link against `cwt::cucumber`, `cwt::cucumber-no-main` or `cwt::cucumber-c`

## Build the Conan Package & Examples

Move to `./package` and create the conan package:

```
cd package
conan create . --version 1.0.0 --user cwt --channel stable
```

If you want to use another user and channel, feel free to do so. But remember to use them correctly in the consumer's `conanfile.txt`
  
And now you can move over to `./consumer` to build the examples: 

```
cd ../consumer
conan install . -of ./build 
cmake -S . -B ./build -DCMAKE_TOOLCHAIN_FILE=./build/conan_toolchain.cmake 
cmake --build ./build
```

## Run the Examples

The three executables are in the build directory: 
- `./build/bin/box` The C++ implementation
- `./build/bin/box-no-main` The C++ implementation with its own main
- `./build/bin/box-c` The C implementation


Navigate (when not already in this directory):
```
cd ./consumer
```

And run all features from the `feature` directory:

```
./build/bin/box ./features
```

Or with an own `main`
```
./build/bin/box-no-main ./features
```

The C implementation supports all features, but you can not run all feature files from a directory, you have to run them explicitly. For instance

```
./build/bin/box-c ./features/first_example.feature ./features/box.feature ./features/scenario_outline.feature
```


