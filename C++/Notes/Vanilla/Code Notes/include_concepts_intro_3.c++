#include <iostream>
#include <concepts> // Needed for using std::convertible_to

// RUN WITH g++ -O3 -std=c++20 -o include_concepts_intro_3 include_concepts_intro_3.c++
// =====================================================
// ✅ CUSTOM CONCEPT #1: TinyType
// =====================================================
// This concept checks whether the size of a type is <= 4 bytes
// ⚠️ Note: The outer 'requires (T t)' block validates the *syntax*,
// but only the nested `requires sizeof(T) <= 4` actually *enforces* the constraint.

template <typename T>
concept TinyType = requires(T t) {
    sizeof(T) <= 4;                // ✅ Valid syntax, but NOT enforced
    requires sizeof(T) <= 4;       // ✅ This enforces the constraint at compile-time
};

// =====================================================
// ✅ CUSTOM CONCEPT #2: Addable
// =====================================================
// This concept checks if the expression `a + b` is valid,
// and whether the result can be converted to `int`
// It uses a Compound Requirement (inside `{}` with `-> convertible_to<type>`)

template <typename T>
concept Addable = requires(T a, T b) {
    { a + b } -> std::convertible_to<int>; 
    // ✅ Check that:
    // - `a + b` is valid syntax
    // - The result can be converted to int
};

// =====================================================
// ✅ Generic Function `add()` restricted to Addable types
// =====================================================
// - Only accepts types that satisfy the Addable concept
// - Works for types where `a + b` is valid and produces a result convertible to int

Addable auto add(Addable auto a, Addable auto b) {
    return a + b;
}

// =====================================================
// ✅ MAIN FUNCTION
// =====================================================
int main() {
    // ================================
    // ✅ EXAMPLE 1: double
    // ================================
    double x{67};
    double y{56};

    // Result of x + y is 123.0, a double
    // And since `double` can be implicitly converted to `int`,
    // this satisfies the Addable concept!
    auto result = add(x, y); 

    std::cout << "result          : " << result << std::endl;            // Output: 123
    std::cout << "sizeof(result)  : " << sizeof(result) << " bytes" << std::endl;

    // ================================
    // ❌ EXAMPLE 2: std::string (uncomment to see compiler error)
    // ================================
    /*
    std::string a{"Hello"};
    std::string b{"World"};

    // std::string a + b is valid
    // BUT the result is not convertible to int => Not Addable!
    auto fail = add(a, b); // ❌ Compiler error!
    */

    return 0;
}
