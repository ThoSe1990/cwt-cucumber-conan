from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout
from conan.tools.files import get


class CucumberRecipe(ConanFile):

    name = "cwt-cucumber"

    license = "MIT"
    author = "Thomas Sedlmair, thomas.sedlmair@googlemail.com"
    url = "https://github.com/ThoSe1990/cwt-cucumber"
    description = "A simple C/C++ Cucumber interpreter"
    topics = ("cpp", "bdd", "testing", "cucumber")

    settings = "os", "compiler", "build_type", "arch"
    options = {"no_main": [True, False], "stack_trace": [True, False]}
    default_options = {"no_main": False, "stack_trace": False}

    def source(self):
        get(self, **self.conan_data["sources"][self.version], strip_root=True)

