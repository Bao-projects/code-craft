"""
This file contains strings of hello world code for multiple programming languages.
These strings will be used for testing purposes.
"""

C_HELLO_WORLD = """
#include <stdio.h>

int main() {
    printf("Hello, world!");
    return 0;
}
"""

CPP_HELLO_WORLD = """
#include <iostream>

int main() {
    std::cout << "Hello, world!" << std::endl;
    return 0;
}
"""

JAVA_HELLO_WORLD = """
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
"""

JAVASCRIPT_HELLO_WORLD = 'console.log("Hello, world!");'

PYTHON_HELLO_WORLD = 'print("Hello, world!")'

RUBY_HELLO_WORLD = 'puts "Hello, world!"'
