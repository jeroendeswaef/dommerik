cmake_minimum_required (VERSION 2.6)
project (dommerik)

add_library(FooFunctions FooOBJ.c)
add_executable(dommerik blah.c)
target_link_libraries (dommerik FooFunctions)