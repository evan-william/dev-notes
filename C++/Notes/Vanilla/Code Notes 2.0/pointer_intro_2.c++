// DANGLING POINTER: 
#include <iostream>

int main() {

    // Case 1 : Uninitialized pointer
    std::cout << "\nCase 1 : Uninitialized pointer : " << std::endl;
    int* p_number;
    p_number = nullptr; // Safe: simulate uninitialized with nullptr
    if (p_number != nullptr) {
        std::cout << "p_number : " << p_number << std::endl;
        std::cout << "*p_number : " << *p_number << std::endl;
    } else {
        std::cout << "p_number is nullptr (would crash if dereferenced)" << std::endl;
    }
    std::cin.get(); // Pause

    // Case 2 : Deleted pointer
    std::cout << "\nCase 2 : Deleted pointer" << std::endl;
    int* p_number1{ new int{67} };

    std::cout << "*p_number1 (before delete) : " << *p_number1 << std::endl;

    delete p_number1;

    p_number1 = nullptr; // Safe: simulate crash prevention
    if (p_number1 != nullptr) {
        std::cout << "*p_number1(after delete) : " << *p_number1 << std::endl;
    } else {
        std::cout << "p_number1 is nullptr (memory deleted)" << std::endl;
    }
    std::cin.get(); // Pause

    // Case 3 : Multiple pointers pointing to same address
    std::cout << "\nCase 3 : Multiple pointers pointing to same address : " << std::endl;

    int* p_number3{ new int{83} };
    int* p_number4{ p_number3 };

    std::cout << "p_number3 - " << p_number3 << " - " << *p_number3 << std::endl;
    std::cout << "p_number4 - " << p_number4 << " - " << *p_number4 << std::endl;

    delete p_number3;

    p_number3 = nullptr;
    if (p_number4 != nullptr) {
        std::cout << "p_number4(after deleting p_number3) - " << p_number4
                  << " - [DANGEROUS: memory deleted, access skipped]" << std::endl;
    }
    std::cin.get(); // Pause

    // Solution 1 :
    std::cout << "\nSolution 1 : " << std::endl;
    int* p_number5{ nullptr };
    int* p_number6{ new int(87) };

    // Check for nullptr before use
    if (p_number6 != nullptr) {
        std::cout << "*p_number6 : " << *p_number6 << std::endl;
    } else {
        std::cout << "Invalid address" << std::endl;
    }
    delete p_number6;
    std::cin.get(); // Pause

    // Solution 2 :
    std::cout << "\nSolution 2 : " << std::endl;
    int* p_number7{ new int{82} };

    // Use the pointer however you want
    std::cout << "p_number7 - " << p_number7 << " - " << *p_number7 << std::endl;

    delete p_number7;
    p_number7 = nullptr; // Reset the pointer

    // Check for nullptr before use
    if (p_number7 != nullptr) {
        std::cout << "*p_number7 : " << *p_number7 << std::endl;
    } else {
        std::cout << "Invalid memory access!" << std::endl;
    }
    std::cin.get(); // Pause

    // Solution 3
    std::cout << "\nSolution 3 : " << std::endl;
    int* p_number8{ new int{382} }; // Let's say p_number8 is the master pointer
    int* p_number9{ p_number8 };

    // Dereference the pointers and use them
    std::cout << "p_number8 - " << p_number8 << " - " << *p_number8 << std::endl;

    if (!(p_number8 == nullptr)) { // Only use slave pointers when master pointer is valid
        std::cout << "p_number9 - " << p_number9 << " - " << *p_number9 << std::endl;
    }

    delete p_number8; // Master releases the memory
    p_number8 = nullptr;

    if (!(p_number8 == nullptr)) { // Only use slave pointers when master pointer is valid
        std::cout << "p_number9 - " << p_number9 << " - " << *p_number9 << std::endl;
    } else {
        std::cerr << "WARNING : Trying to use an invalid pointer" << std::endl;
    }

    std::cout << "\nProgram is ending well" << std::endl;

    return 0;
}
