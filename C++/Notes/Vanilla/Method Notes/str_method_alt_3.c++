#include <iostream>
#include <cstring>

int main() {
    // ================================
    // 1. std::strcat - Concatenation
    // ================================
    std::cout << "\n=== std::strcat ===\n";

    char dest[100] = "Hello ";
    char src[50] = "World!";

    std::strcat(dest, src);  // Append "World!" to "Hello "
    std::cout << "After first strcat: " << dest << std::endl; // Hello World!

    std::strcat(dest, " Goodbye World!");
    std::cout << "After second strcat: " << dest << std::endl; // Hello World! Goodbye World!


    // ===============================================
    // 2. std::strcat - Using dynamically allocated memory
    // ===============================================
    std::cout << "\n=== More std::strcat (Dynamic Memory) ===\n";

    char* dest1 = new char[100]{'F','i','r','e','l','o','r','d','\0'}; // "Firelord"
    char* source1 = new char[100]{',','T','h','e',' ','P','h','e','n','i','x',' ','K','i','n','g','!','\0'}; // ",The Phenix King!"

    std::cout << "Before concat:\n";
    std::cout << "dest1: " << dest1 << std::endl;
    std::cout << "source1: " << source1 << std::endl;

    std::strcat(dest1, source1); // Append source1 to dest1
    std::cout << "After strcat:\n";
    std::cout << "dest1: " << dest1 << std::endl;

    delete[] dest1;
    delete[] source1;


    // ================================
    // 3. std::strncat - Limit characters
    // ================================
    std::cout << "\n=== std::strncat ===\n";

    char dest2[100] = "Hello";
    char source2[50] = " There is a bird on my window";

    std::strncat(dest2, source2, 6); // Append only 6 chars: " There"
    std::cout << "After strncat: " << dest2 << std::endl;


    // ================================
    // 4. std::strcpy - Copy full string
    // ================================
    std::cout << "\n=== std::strcpy ===\n";

    const char* source3 = "C++ is a multipurpose programming language.";
    char* dest3 = new char[std::strlen(source3) + 1]; // +1 for null-terminator

    std::strcpy(dest3, source3);
    std::cout << "Copied string: " << dest3 << std::endl;

    delete[] dest3;


    // ================================
    // 5. std::strncpy - Copy limited characters
    // ================================
    std::cout << "\n=== std::strncpy ===\n";

    const char* source4 = "Hello";
    char dest4[] = {'a', 'b', 'c', 'd', 'e', 'f','g','h','\0'}; // Initial dummy data

    std::cout << "Before strncpy, dest4: " << dest4 << std::endl;

    std::strncpy(dest4, source4, 5); // Copy only 5 characters
    std::cout << "After strncpy, dest4: " << dest4 << std::endl;

    return 0;
}
