#include <iostream>

// ======================
// PASSING PARAMETER (BY VALUE)
// ======================

void say_age_by_value(int age) {
    // This function receives a copy of the original variable.
    // Modifications here do NOT affect the original value.
    ++age;
    std::cout << "[BY VALUE] Hello, you are " << age << " years old! ";
    std::cout << "&age (inside): " << &age << std::endl;
}

// ======================
// PASSING PARAMETER (BY POINTER)
// ======================

void say_age_by_pointer(int* age) {
    // This function receives a pointer (address) to the original variable.
    // Dereferencing (*) allows us to modify the original variable.
    ++(*age);
    std::cout << "[BY POINTER] Hello, you are " << *age << " years old! ";
    std::cout << "&*age (original): " << age << std::endl;
}

// ======================
// PASSING PARAMETER (BY REFERENCE)
// ======================

void say_age_by_reference(int& age) {
    // This function receives a reference to the original variable.
    // It's like an alias, so any modification directly affects the original.
    ++age;
    std::cout << "[BY REFERENCE] Hello, you are " << age << " years old! ";
    std::cout << "&age (inside): " << &age << std::endl;
}

// ======================
// MAIN FUNCTION
// ======================

int main() {
    // === By Value ===
    int age1{23};
    std::cout << "=== PASS BY VALUE ===" << std::endl;
    std::cout << "Before call: age1 = " << age1 << ", &age1: " << &age1 << std::endl;
    say_age_by_value(age1);
    std::cout << "After call : age1 = " << age1 << ", &age1: " << &age1 << std::endl;

    std::cout << "\n==============================\n" << std::endl;

    // === By Pointer ===
    int age2{23};
    std::cout << "=== PASS BY POINTER ===" << std::endl;
    std::cout << "Before call: age2 = " << age2 << ", &age2: " << &age2 << std::endl;
    say_age_by_pointer(&age2); // Pass address
    std::cout << "After call : age2 = " << age2 << ", &age2: " << &age2 << std::endl;

    std::cout << "\n==============================\n" << std::endl;

    // === By Reference ===
    int age3{23};
    std::cout << "=== PASS BY REFERENCE ===" << std::endl;
    std::cout << "Before call: age3 = " << age3 << ", &age3: " << &age3 << std::endl;
    say_age_by_reference(age3);
    std::cout << "After call : age3 = " << age3 << ", &age3: " << &age3 << std::endl;

    return 0;
}
