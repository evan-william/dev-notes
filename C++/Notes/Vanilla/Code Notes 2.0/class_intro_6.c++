#include <iostream>
#include <string> // Required to use std::string

// =========================
// CLASS SIZE ANALYSIS
// =========================

// Define a class named Dog
class Dog {
public:
    Dog() = default; // Default constructor

    void prin_info() {
        // Member function that does nothing.
        // Member functions do not affect the size of the class.
    }

    void do_something() {
        // Another member function that does nothing.
        // Like all member functions, this does not contribute to sizeof(Dog).
    }

private:
    // === MEMBER VARIABLES ===

    size_t leg_count;   // Typically 8 bytes on 64-bit systems
    size_t arm_count;   // Another 8 bytes
    int* p_age;         // A pointer to int, typically 8 bytes on 64-bit systems

    // Total size from member variables = 8 + 8 + 8 = 24 bytes
    // However, due to alignment and padding, the actual sizeof(Dog) might be more than this.
};

int main() {
    Dog dog1;

    // === BASIC TYPE SIZES ===

    std::cout << "sizeof(size_t) : " << sizeof(size_t) << std::endl;
    // Output: 8 on a 64-bit system. size_t is an unsigned integer type used to represent sizes.

    std::cout << "sizeof(int*) : " << sizeof(int*) << std::endl;
    // Output: 8 on a 64-bit system. A pointer takes 8 bytes (memory address width).

    std::cout << "sizeof(Dog) : " << sizeof(dog1) << std::endl;
    // Expected: Likely 24 bytes or possibly more (e.g. 24, 32) due to alignment.
    // Explanation:
    // - Each size_t is 8 bytes
    // - The pointer (int*) is also 8 bytes
    // - So raw total is 24 bytes
    // - Compilers may add padding to ensure proper memory alignment for performance.
    //   e.g., making the total size a multiple of 8 or 16 bytes.
    // - Member functions do not add to class size because all instances share function code.
    // - No virtual functions means no vtable pointer added.

    // === STRING SIZE ===

    std::string name{"I am the king of the universe!"};

    std::cout << "sizeof(name) : " << sizeof(name) << std::endl;
    // Output: Typically 32 bytes on most 64-bit libstdc++ implementations
    // Explanation:
    // - std::string is a class with internal pointers and size fields.
    // - sizeof(name) only returns the size of the std::string object itself
    //   (i.e., the object on the stack, not the actual character data in memory).
    // - The character data is stored on the heap (dynamically allocated),
    //   and sizeof does not account for heap allocations.

    return 0;
}
