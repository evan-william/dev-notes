#include <iostream>
#include <concepts> // Required for using concepts like std::integral

// RUN WITH g++ -O3 -std=c++20 -o include_concepts_intro include_concepts_intro.c++
// ----------------------------
// Concepts in C++20 allow you to put constraints on template parameters.
// std::integral is a built-in concept that checks if a type is an integer type
// (like int, char, long, etc. — NOT float or double).
// If the constraint is not satisfied, you'll get a compile-time error.
// ----------------------------

// Syntax 1: traditional syntax using `requires` clause after template definition
template <typename T>
requires std::integral<T>
T add1(T a, T b) {
    return a + b;
}

// Syntax 2: concept applied directly to the template parameter
template <std::integral T>
T add2(T a, T b) {
    return a + b;
}

// Syntax 3: concept applied inline with function parameters (auto requires std::integral)
auto add3(std::integral auto a, std::integral auto b) {
    return a + b;
}

// Syntax 4: trailing `requires` clause (equivalent to Syntax 1)
template <typename T>
T add4(T a, T b) requires std::integral<T> {
    return a + b;
}

int add(std::integral auto a, std::integral auto b) {
    return a;
}

int main() {
    char a_0{10};
    char a_1{20};

    // Syntax 1 usage
    auto result1 = add1(a_0, a_1);
    std::cout << "[Syntax1] result1 (char): " << static_cast<int>(result1) << std::endl;

    // Syntax 2 usage
    int b_0{11};
    int b_1{5};
    auto result2 = add2(b_0, b_1);
    std::cout << "[Syntax2] result2 (int): " << result2 << std::endl;

    // Syntax 3 usage
    long c_0{1000};
    long c_1{2500};
    auto result3 = add3(c_0, c_1);
    std::cout << "[Syntax3] result3 (long): " << result3 << std::endl;

    // Syntax 4 usage
    short d_0{300};
    short d_1{500};
    auto result4 = add4(d_0, d_1);
    std::cout << "[Syntax4] result4 (short): " << result4 << std::endl;

    // Uncommenting this will cause a compile-time error
    // because `double` is NOT an integral type.
    /*
    double e_0{11.1};
    double e_1{1.9};
    auto result5 = add1(e_0, e_1); // Error: double does not satisfy std::integral
    std::cout << "result5 (double): " << result5 << std::endl;
    */

    return 0;
}
