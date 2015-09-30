cmake_minimum_required (VERSION 2.6)
project (dommerik)

add_library(NodeFunctions NodeOBJ.c)
add_executable(dommerik main.c)
target_link_libraries (dommerik NodeFunctions)