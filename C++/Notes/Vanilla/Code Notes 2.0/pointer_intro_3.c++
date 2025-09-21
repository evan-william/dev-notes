#include <iostream>

// NULL POINTER SAFETY AND MEMORY LEAKS

int main() {
    // Verbose nullptr check
    std::cout << std::endl;
    std::cout << "Verbose nullptr check: " << std::endl;

    int *p_number{};  // Initialized to nullptr (same as 'int *p_number = nullptr;')

    // Verbose check if pointer is valid or not
    if (p_number) {
        std::cout << "p_number points to a VALID address: " << p_number << std::endl;
        std::cout << "*p_number: " << *p_number << std::endl;
    } else {
        std::cout << "p_number points to an INVALID address." << std::endl;
    }

    // You should never attempt to delete a nullptr as it causes undefined behavior.
    // However, calling delete on nullptr is safe in C++.
    delete p_number;  // Safe, since p_number is nullptr

    // It is OK to call delete on a nullptr (no crash, no errors)
    int *p_number1{}; 
    delete p_number1;  // Safe, does nothing as p_number1 is nullptr

    // // Another way to check before delete:
    // if (p_number1 != nullptr) {
    //     delete p_number1;
    // }

    std::cout << std::endl;

    // MEMORY LEAK EXAMPLES:

    // Memory Leak Example 1: Pointer loses reference to allocated memory
    {
        int *p_number = new int{67};  // Allocated memory on heap

        // Should delete and reset here to avoid a memory leak

        int number{55}; // Stack variable (automatically destroyed when it goes out of scope)
        
        // Now p_number points to the stack variable 'number', but the memory allocated earlier is lost
        p_number = &number;  // Memory at p_number's previous address is now leaked (lost)

        // Memory leak occurs because we lost access to the memory allocated for int{67}, but it's still occupied in memory
        // The allocated memory was not deleted before losing the reference to it.
    }

    // Memory Leak Example 2: Double allocation without deleting old memory
    {
        int *p_number1 = new int{55};  // Allocated memory for int{55}

        // We use p_number1 for some time here... 

        // Later, we assign a new memory block to p_number1 without deleting the old one
        p_number1 = new int{44};  // The memory holding int{55} is now leaked (lost)

        // Always delete dynamically allocated memory when done
        delete p_number1;   // Properly deleting the most recent allocation
        p_number1 = nullptr; // Reset pointer to nullptr to avoid dangling pointer
    }

    // Memory Leak Example 3: Nested scope with dynamically allocated memory
    {
        int *p_number2 = new int{57};  // Allocated memory for int{57}

        // We use p_number2 here...

    }  // Memory allocated for p_number2 is leaked as we leave the scope without deleting it

    std::cout << "Program ending well" << std::endl;

    // STD NO THROW EXPLANATION:
    /*
    new(std::nothrow) will attempt to allocate memory for 1000 integers, but instead of throwing an exception (std::bad_alloc) if it fails, it will return nullptr.
    You can then check if the allocation succeeded by checking if data is nullptr.
    */

    // New Example with arrays, dynamically allocated memory and initialization:
    const size_t size{10};

    // Different ways you can declare an array dynamically and how they are initialized
    double *p_salaries { new double[size]}; // salaries array will contain garbage values
    int *p_students { new(std::nothrow) int[size]{} }; // All values initialized to 0 

    double *p_scores { new(std::nothrow) double[size]{1,2,3,4,5}}; // Allocating memory space
                                                                  // for an array of size double
                                                                  // vars. First 5 will be initialized
                                                                  // with 1,2,3,4,5, and the rest will be 0's.

    // nullptr check and use the allocated array
    if(p_scores){
        std::cout << "size of scores (it's a regular pointer): " << sizeof(p_scores) << std::endl;
        std::cout << "Successfully allocated memory for scores."<< std::endl;
        
        // Print out elements. Can use regular array access notation, or pointer arithmetic
        for(size_t i{}; i < size; ++i){
            std::cout << "value : " << p_scores[i] << " : " << *(p_scores + i) << std::endl;
        }
    } else {
        std::cout << "Memory allocation for scores failed!" << std::endl;
    }

    delete[] p_salaries;
    p_salaries = nullptr;

    delete[] p_students;
    p_students = nullptr;

    delete[] p_scores;
    p_scores = nullptr;

    // Static arrays Vs dynamic arrays
    std::cout << "=====================================" << std::endl;

    // Static array (lives on the stack)
    int scores[10] {1,2,3,4,5,6,7,8,9,10};
    std::cout << "scores size: " << std::size(scores) << std::endl;
    for(auto s : scores){
        std::cout << "value: " << s << std::endl;
    }

    // Dynamic array (lives on the heap)
    int* p_scores1 = new int[10] {1,2,3,4,5,6,7,8,9,10}; // Lives on the heap
    std::cout << "p_scores1 values: " << std::endl;
    for(size_t i{}; i < 10; ++i){
        std::cout << "value: " << p_scores1[i] << std::endl;
    }

    delete[] p_scores1;
    p_scores1 = nullptr;

    return 0;
}
