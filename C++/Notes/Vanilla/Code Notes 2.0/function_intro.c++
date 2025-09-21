#include <iostream>

//====================== Function Definitions ============================

// 1. Function that takes a parameter but returns nothing
void enter_bar(size_t age) {
    if (age > 18) {
        std::cout << "You're " << age << " years old. Please proceed." << std::endl;
    } else {
        std::cout << "Sorry, you're too young for this. No offense!" << std::endl;
    }
    return;
}

// 2. Function that takes parameters and returns a value
int max(int a, int b) {
    if (a > b)
        return a;
    else
        return b;
}

// 3. Function that takes no parameters and returns nothing
void say_hello() {
    std::cout << "Hello there!" << std::endl;
    return; // Optional in void functions
}

// 4. Function that takes no parameters and returns something
int lucky_number() {
    return 99;
}

// 5. Function with pass-by-value (copies), modifies inside only
double increment_multiply(double a, double b) {
    std::cout << "[Inside function BEFORE increment]" << std::endl;
    std::cout << "a: " << a << ", b: " << b << std::endl;

    double result = (++a) * (++b); // Pre-increment a and b, then multiply

    std::cout << "[Inside function AFTER increment]" << std::endl;
    std::cout << "a: " << a << ", b: " << b << std::endl;

    return result;
}

//=========================== MAIN FUNCTION =============================

int main() {

    // 1. Testing enter_bar (parameter, no return)
    std::cout << "\n=== Testing enter_bar ===\n";
    enter_bar(22); // Adult
    enter_bar(15); // Underage

    // 2. Testing max (with return)
    std::cout << "\n=== Testing max ===\n";
    int x{22};
    int y{44};
    std::cout << "Max between " << x << " and " << y << " is: " << max(x, y) << std::endl;

    // 3. Testing say_hello (no parameter, no return)
    std::cout << "\n=== Testing say_hello ===\n";
    say_hello();

    // 4. Testing lucky_number (no parameter, returns value)
    std::cout << "\n=== Testing lucky_number ===\n";
    int result = lucky_number();
    std::cout << "Your lucky number is: " << result << std::endl;

    // 5. Testing increment_multiply (pass-by-value behavior)
    std::cout << "\n=== Testing increment_multiply ===\n";
    double h{3.0};
    double i{4.0};

    std::cout << "[Outside function BEFORE call]" << std::endl;
    std::cout << "h: " << h << ", i: " << i << std::endl;

    double incr_mult_result = increment_multiply(h, i);

    std::cout << "[Outside function AFTER call]" << std::endl;
    std::cout << "h: " << h << ", i: " << i << std::endl;
    std::cout << "Result ( (h+1)*(i+1) ): " << incr_mult_result << std::endl;

    
    return 0;
}
