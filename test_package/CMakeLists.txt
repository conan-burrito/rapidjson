cmake_minimum_required(VERSION 3.6)
project(PackageTest VERSION 1.0.0 LANGUAGES CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_executable(example example.cpp)
target_link_libraries(example CONAN_PKG::rapidjson)
set_target_properties(example PROPERTIES OUTPUT_NAME "test")
