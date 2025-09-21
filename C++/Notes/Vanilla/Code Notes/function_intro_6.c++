// TemplateTypeDeductionAndExplicitArgument
#include <iostream>
#include <string>

// Generic function template to return the maximum of two values (by value)
template <typename T>
T maximum(T a, T b) {
    return (a > b) ? a : b;
}

// 🔧 Forward declaration of the reference version
template <typename T>
const T& maximum_ref(const T& a, const T& b);

int main() {

    // 1. Example with int values - compiler will deduce T as int
    int a{10};
    int b{23};
    auto max1 = maximum(a, b); // T is deduced as int
    std::cout << "max1 (int): " << max1 << std::endl;

    // 2. Example with double values - compiler will deduce T as double
    double c{34.7};
    double d{23.4};
    auto max2 = maximum(c, d); // T is deduced as double
    std::cout << "max2 (double): " << max2 << std::endl;

    // 3. Example with strings - compiler will deduce T as std::string
    std::string e{"hello"};
    std::string f{"world"};
    auto max3 = maximum(e, f); // T is deduced as std::string
    std::cout << "max3 (string): " << max3 << std::endl;

    // 4. Using explicit template argument - forces conversion from int to double
    auto max4 = maximum<double>(a, b); // a and b are int, but T is forced to double
    std::cout << "max4 (explicit double): " << max4 << std::endl;

    // 5. ❌ This will cause a compile-time error - cannot convert std::string to double
    // auto max5 = maximum<double>(a, f); // ERROR: 'f' (string) can't convert to double
    // std::cout << "max5: " << max5 << std::endl;

    // ⚠️ Uncommenting the lines above will cause the program to fail compilation

    // --------------------------------------------
    // Extension: TemplateTypeParameterByReference
    // --------------------------------------------

    double x{23.5};
    double y{51.2};

    std::cout << "\n=== Using maximum_ref (by reference) ===" << std::endl;
    std::cout << "Out - &x: " << &x << std::endl;
    auto result = maximum_ref(x, y); // Calls the by-reference version
    std::cout << "Result: " << result << std::endl;
    std::cout << "Out - &x: " << &x << std::endl;

    return 0;
}

// Reference version: avoids copying large objects and returns a reference
template <typename T>
const T& maximum_ref(const T& a, const T& b) {
    std::cout << "In  - &a: " << &a << std::endl;
    return (a > b) ? a : b;
}

/*
⚠️ WARNING: Do not define both of these with the same name `maximum`:
    - T maximum(T a, T b)           --> by value
    - const T& maximum(const T&, const T&) --> by reference

Why?
- Both can match the same call like `maximum(5, 10)`
- This causes **ambiguity** in overload resolution
- The compiler won’t know which one to choose and will throw an error

✅ Tip:
- If you need both, use different function names (e.g., `maximum` and `maximum_ref`)
- Or use concepts or SFINAE (advanced topic) to make selection smarter
- For most cases, prefer the reference version (`maximum_ref`) to avoid unnecessary copies
*/
