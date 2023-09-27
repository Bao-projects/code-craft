"""
This file contains strings of hello world code for multiple programming languages.
These strings will be used for testing purposes.
"""

C_HELLO_WORLD = """
#include <stdio.h>

int main() {
    printf("Hello, world! by C");
    return 0;
}
"""

CPP_HELLO_WORLD = """
#include <iostream>

int main() {
    std::cout << "Hello, world! by C++" << std::endl;
    return 0;
}
"""

JAVA_HELLO_WORLD = """
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World! by Java");
    }
}
"""

JAVASCRIPT_HELLO_WORLD = 'console.log("Hello, world! by Javascript");'

PYTHON_HELLO_WORLD = 'print("Hello, world! by Python")'

RUBY_HELLO_WORLD = 'puts "Hello, world! by Ruby"'
