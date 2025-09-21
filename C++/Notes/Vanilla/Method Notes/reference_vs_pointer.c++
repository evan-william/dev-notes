#include <iostream>

int main() {
    int a = 5;

    // Reference
    int& ref = a;
    std::cout << ref << std::endl;   // 5
    std::cout << &ref << std::endl;  // memory address of a

    // Pointer
    int* ptr = &a;
    std::cout << *ptr << std::endl;  // 5
    std::cout << ptr << std::endl;   // memory address of a
}
