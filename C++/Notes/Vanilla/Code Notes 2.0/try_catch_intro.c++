#include <iostream>

int main() {

    // Using try-catch to safely handle memory allocation failures
    for (size_t i{0}; i < 100; ++i) {
        try {
            int * data = new int[1000000000];
            std::cout << "Data allocated" << std::endl;
            delete[] data; // prevent memory leak (delete[] tells the compiler, “This pointer points to an array. Free it correctly.”)
        } catch (std::exception& ex) {
            std::cout << "Something went wrong: " << ex.what() << std::endl;
        }
    }

    std::cout << "Program ending well" << std::endl;

    return 0;
}
