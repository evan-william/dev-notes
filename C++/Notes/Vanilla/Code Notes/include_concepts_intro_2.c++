#include <iostream>
#include <type_traits>
#include <concepts>
#include <string> // Needed for std::string

// RUN WITH g++ -O3 -std=c++20 -o include_concepts_intro_2 include_concepts_intro_2.c++
// =========================
// CUSTOM CONCEPT #1: MyIntegral
// =========================
// This concept accepts only integral types: int, long, short, char, etc.
template <typename T>
concept MyIntegral = std::is_integral_v<T>; 
// uses SFINAE to check if std::is_integral<T>::value == true OR FALSE, if false gonna fail

// ✅ Function that accepts only integral types (like int, long, etc)
MyIntegral auto add_integers(MyIntegral auto a, MyIntegral auto b) {
    return a + b;
} 

// =========================
// CUSTOM CONCEPT #2: Multipliable
// =========================
// Accepts any type where the expression a * b is valid.
template <typename T>
concept Multipliable = requires(T a, T b) {
    a * b; // ensures a * b is valid syntax
};

// =========================
// CUSTOM CONCEPT #3: Incrementable
// =========================
// Accepts any type where a+=1, ++a, and a++ are all valid.
// This ensures the type supports typical arithmetic increments.
template <typename T>
concept Incrementable = requires(T a) {
    a += 1;
    ++a;
    a++;
};

// ✅ Function restricted to types that satisfy Incrementable
// - Only types that can be incremented (like int, double) will compile
// - Strings, for example, do NOT satisfy this concept
template <typename T>
requires Incrementable<T> // THIS HAS SAME STYLE WITH THE BELOW!
T add(T a, T b) {
    return a + b;
}

/* SAME AS ABOVE JUST DIFF STYLE
Incrementable auto add(Incrementable auto a, Incrementable auto b) {
    return a + b;
}
*/

int main() {
    // ==============================
    // EXAMPLE 1: double - allowed
    // ==============================
    double x{6};
    double y{7};

    std::cout << "Adding doubles: " << add(x, y) << std::endl; // ✅ Works: double is Incrementable

    // ==============================
    // EXAMPLE 2: std::string - NOT allowed with add()
    // ==============================
    /*
    std::string x{"Hello"};
    std::string y{"World"};

    std::cout << add(x, y); // ❌ ERROR: std::string is NOT Incrementable (no x += 1 or x++)
    */

    // ==============================
    // EXAMPLE 3: int - allowed by MyIntegral concept
    // ==============================
    int a = 3;
    int b = 4;

    std::cout << "Adding integers: " << add_integers(a, b) << std::endl; // ✅ Works: int is MyIntegral

    return 0;
}
