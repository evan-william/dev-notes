#include <iostream>  // For standard input-output
#include <cstring>   // For C-style string functions like strlen, strcmp, strchr, etc.

int main() {

    // ======== strlen and sizeof ========
    std::cout << "=== strlen and sizeof ===\n";

    const char message1[] = "The sky is blue.";  
    // message1 is a character array initialized with a string literal.
    // The compiler automatically appends '\0' at the end of the array.

    const char* message2 = "The sky is blue.";  
    // message2 is a pointer to a string literal (resides in read-only memory).

    std::cout << "message1 : " << message1 << std::endl;
    std::cout << "strlen(message1) : " << std::strlen(message1) << std::endl;
    // strlen() counts the number of characters before the null terminator '\0'.
    // So output will be 16, as "The sky is blue." has 16 visible characters.

    std::cout << "sizeof(message1) : " << sizeof(message1) << std::endl;
    // sizeof() gives the total size in bytes of the array, including '\0'.
    // So output will be 17.

    std::cout << "strlen(message2) : " << std::strlen(message2) << std::endl;
    // Same as above, returns 16.

    std::cout << "sizeof(message2) : " << sizeof(message2) << std::endl;
    // This is different! message2 is a pointer.
    // sizeof(message2) returns the size of the pointer (usually 8 bytes on 64-bit systems).



    // ======== strcmp ========
    std::cout << "\n=== std::strcmp ===\n";
    
    // strcmp() compares two C-style strings lexicographically.
    // It returns:
    //   < 0 if s1 < s2
    //   0   if s1 == s2
    //   > 0 if s1 > s2

    const char* s1 = "Alabama";
    const char* s2 = "Blabama";
    std::cout << "strcmp(Alabama, Blabama) = " << std::strcmp(s1, s2) << std::endl;
    // Returns a negative value because 'A' < 'B' lexicographically

    s1 = "Alabama";
    s2 = "Alabamb";
    std::cout << "strcmp(Alabama, Alabamb) = " << std::strcmp(s1, s2) << std::endl;
    // Returns a negative value because after matching "Alabam", 'a' < 'b'

    s1 = "Alacama";
    s2 = "Alabama";
    std::cout << "strcmp(Alacama, Alabama) = " << std::strcmp(s1, s2) << std::endl;
    // Returns positive because at position 4, 'c' > 'b'

    s1 = "India";
    s2 = "France";
    std::cout << "strcmp(India, France) = " << std::strcmp(s1, s2) << std::endl;
    // Returns positive because 'I' > 'F'

    s1 = "Kigali";
    s2 = "Kigali";
    std::cout << "strcmp(Kigali, Kigali) = " << std::strcmp(s1, s2) << std::endl;
    // Returns 0 because the strings are equal



    // ======== strncmp (first n chars only) ========
    std::cout << "\n=== std::strncmp ===\n";
    
    s1 = "aaaia";
    s2 = "aaance";
    size_t n = 3;
    std::cout << "strncmp(aaaia, aaance, 3) = " << std::strncmp(s1, s2, n) << std::endl;
    // Compares first 3 characters: 'a', 'a', 'a' vs 'a', 'a', 'a' => equal => 0

    n = 5;
    std::cout << "strncmp(aaaia, aaance, 5) = " << std::strncmp(s1, s2, n) << std::endl;
    // Compares first 5 characters: 'aaaia' vs 'aaanc'
    // At position 3: 'i' > 'n' => returns positive

    s1 = "aaaoa";
    std::cout << "strncmp(aaaoa, aaance, 5) = " << std::strncmp(s1, s2, n) << std::endl;
    // At position 3: 'o' > 'n' => returns positive again



    // ======== strchr: find first occurrence of char ========
    std::cout << "\n=== std::strchr ===\n";
    
    const char* str = "Try not. Do, or do not. There is no try.";
    char target = 'T';  // Target character to search for

    const char* result = str;  // Start from beginning of string
    size_t iterations = 0;     // Count how many times 'T' is found

    while ((result = std::strchr(result, target)) != nullptr) { // IF NO FIND TARGET IT WILL RETURN NULLPTR
        // strchr() returns a pointer to the first occurrence of 'T' starting from 'result'
        std::cout << "Found '" << target << "' at: " << result << '\n';
        ++result;  // Move one character ahead to avoid finding the same character again
        ++iterations;
    }
    std::cout << "Total occurrences: " << iterations << std::endl;
    // This loop prints all positions where 'T' is found and counts them



    // ======== strrchr: find last occurrence of char ========
    std::cout << "\n=== std::strrchr ===\n";
    
    char input[] = "/home/user/hello.cpp";
    char* last_slash = std::strrchr(input, '/');  
    // strrchr() finds the last occurrence of '/' in the string

    if (last_slash) {
        std::cout << "Filename: " << (last_slash + 1) << std::endl;
        // Move one character after '/' to get just the filename ("hello.cpp")
    }

    return 0;
}
