cmake_minimum_required(VERSION 3.31)
project(projekts)

set(CMAKE_CXX_STANDARD 20)

add_executable(projekts main.cpp
        Numbers.cpp
        Numbers.h
        Words.cpp
        Words.h)
