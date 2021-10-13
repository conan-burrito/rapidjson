from conans import tools, ConanFile, CMake

import os


class RapidJSON(ConanFile):
    name = 'rapidjson'
    description = 'A fast JSON parser/generator for C++ with both SAX/DOM style API'
    homepage = 'https://github.com/Tencent/rapidjson'
    license = 'MIT'
    url = 'https://github.com/conan-burrito/rapidjson'
    generators = 'cmake'
    no_copy_source = True


    @property
    def source_subfolder(self):
        return 'src'

    def source(self):
       tools.get(**self.conan_data["sources"][self.version], strip_root=True, destination=self.source_subfolder)

    def build(self):
        args = [
            '-DRAPIDJSON_BUILD_DOC=OFF',
            '-DRAPIDJSON_BUILD_EXAMPLES=OFF',
            '-DRAPIDJSON_BUILD_TESTS=OFF'
        ]

        cmake = CMake(self)
        cmake.configure(args=args, source_folder=self.source_subfolder)
        cmake.build(target='install')

    def package_id(self):
        self.info.header_only()

    def package_info(self):
        self.cpp_info.names["cmake_find_package"] = "RapidJSON"
        self.cpp_info.names["cmake_find_package_multi"] = "RapidJSON"

