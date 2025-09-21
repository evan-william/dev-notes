#include <iostream>
#include <concepts> // Required for concepts like std::integral, std::floating_point


// RUN WITH g++ -O3 -std=c++20 -o include_concepts_intro_4 include_concepts_intro_4.c++
// ====================================================
// ✅ CUSTOM CONCEPT: TinyType
// ====================================================
template <typename T>
concept TinyType = requires(T t) {
    sizeof(T) <= 4;          // ✅ Syntax check
    requires sizeof(T) <= 4; // ✅ Enforced rule
};

// ====================================================
// ✅ COMBINED CONCEPT FUNCTION TEMPLATE (named `add`)
// ====================================================
// Works only for integral types AND types <= 4 bytes
template <typename T>
requires std::integral<T> && TinyType<T>
T add(T a, T b) {
    return a + b;
}

// ====================================================
// ✅ ABBREVIATED FUNCTION TEMPLATE USING `auto` WITH CONCEPTS
// ====================================================
// This function only allows integral types (no TinyType constraint here)
std::integral auto add_integral(std::integral auto a, std::integral auto b) {
    return a + b;
}

// Another version that only allows floating-point types
std::floating_point auto add_floating(std::floating_point auto a, std::floating_point auto b) {
    return a + b;
}

// ====================================================
// ✅ MAIN FUNCTION
// ====================================================
int main() {
    // Test original concept-based `add()`
    int a = 10;
    int b = 20;

    auto result = add(a, b); // ✅ Works: int is integral and ≤ 4 bytes
    std::cout << "Result (int, concept-based): " << result << std::endl;

    // long long int x = 7, y = 5;
    // auto error_result = add(x, y); ❌ Compilation error: not TinyType

    // ✅ Test abbreviated template with `std::integral auto`
    auto result2 = add_integral(100, 200); // OK: 100 and 200 are int
    std::cout << "Result (int, abbreviated template): " << result2 << std::endl;

    // ✅ Test abbreviated template with `std::floating_point auto`
    auto result3 = add_floating(5.5, 3.2); // OK: both are double
    std::cout << "Result (float, abbreviated template): " << result3 << std::endl;

    // ❌ auto result4 = add_floating(5, 8); // ERROR: 5 and 8 are integers, not floating-point

    return 0;
}
