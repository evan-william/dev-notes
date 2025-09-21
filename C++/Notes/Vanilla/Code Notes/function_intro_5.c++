// ------------------------------------------------------------------
// FUNCTION TEMPLATE EXAMPLE IN C++
// ------------------------------------------------------------------
// Templates allow us to write generic functions or classes.
// Instead of writing separate functions for int, float, string, etc.,
// we write one "template" and let the compiler generate the actual code
// based on the types passed when calling the function.

#include <iostream>
#include <string>

// -------------------
// FUNCTION TEMPLATE
// -------------------
template <typename T> T maximum(T a , T b) { // Declare a function template with type parameter T 
    // This function works for ANY type T (int, double, string, pointer, etc.)
    // As long as '>' is defined for that type.
    
    // The ternary operator chooses the greater of the two:
    // If a > b is true, return a; otherwise, return b.
    return (a > b) ? a : b;
}

int main(){

    // ----------------------
    // INTEGER COMPARISON
    // ----------------------
    int x{5};
    int y{7};

    // 'maximum<int>' is instantiated automatically
    // T becomes 'int' here
    std::cout << "[int] max(x,y): " << maximum(x, y) << std::endl;
    // Output: 7

    // ----------------------
    // STRING COMPARISON
    // ----------------------
    std::string str1 = "Apple";
    std::string str2 = "Orange";

    // T becomes 'std::string' here
    std::cout << "[string] max(str1,str2): " << maximum(str1, str2) << std::endl;
    // Output: Orange (based on lexicographical comparison)

    // ----------------------
    // DOUBLE COMPARISON
    // ----------------------
    double d1 = 10.5;
    double d2 = 3.14;

    // T becomes 'double' here
    std::cout << "[double] max(d1,d2): " << maximum(d1, d2) << std::endl;
    // Output: 10.5

    // ----------------------
    // POINTER COMPARISON
    // ----------------------
    // Comparing memory addresses, not values!
    int* p_x {&x};
    int* p_y {&y};

    // T becomes 'int*' here (pointer to int)
    // The function compares the ADDRESSES, not the values stored at those addresses
    auto result = maximum(p_x, p_y);

    // *result dereferences the pointer to show the actual value
    std::cout << "[pointer] max(p_x,p_y): " << *result << std::endl;

    // ⚠️ NOTE:
    // The result will depend on memory layout.
    // If &x > &y in memory, you'll get x (5), otherwise y (7)
    // So this comparison is NOT about the values 5 and 7,
    // but rather the numeric values of their addresses in RAM.

    return 0;
}
