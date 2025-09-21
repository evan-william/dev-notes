#include <iostream>
#include <cctype> // For character handling functions like isalpha, isalnum, etc.
#include <cstddef> // For std::size

int main() {

    // ------------------- Check if character is alphanumeric -------------------
    std::cout << "\n=== std::isalnum ===\n";
    std::cout << "C is alphanumeric: " << std::isalnum('C') << std::endl; // 1
    std::cout << "^ is alphanumeric: " << std::isalnum('^') << std::endl; // 0

    char input_char {'*'};
    if (std::isalnum(input_char)) {
        std::cout << input_char << " is alphanumeric.\n";
    } else {
        std::cout << input_char << " is NOT alphanumeric.\n";
    }

    // ------------------- Check if character is alphabetic -------------------
    std::cout << "\n=== std::isalpha ===\n";
    std::cout << "e is alphabetic: " << std::isalpha('e') << std::endl; // 1
    std::cout << "^ is alphabetic: " << std::isalpha('^') << std::endl; // 0
    std::cout << "7 is alphabetic: " << std::isalpha('7') << std::endl; // 0

    if (std::isalpha('e')) {
        std::cout << "'e' is alphabetic\n";
    } else {
        std::cout << "'e' is NOT alphabetic\n";
    }

    // ------------------- Check for blank characters (space or tab) -------------------
    std::cout << "\n=== std::isblank ===\n";
    char message[] {"Hello there. How are you doing? The sun is shining."};
    std::cout << "Message: " << message << std::endl;

    size_t blank_count{};
    for (size_t i{0}; i < std::size(message); ++i) {
        if (std::isblank(message[i])) {
            std::cout << "Found a blank character at index: [" << i << "]\n";
            ++blank_count;
        }
    }
    std::cout << "Total blank characters found: " << blank_count << "\n";

    // ------------------- Check if character is lowercase or uppercase -------------------
    std::cout << "\n=== std::islower and std::isupper ===\n";
    char thought[] {"The C++ Programming Language is one of the most used on the Planet"};
    size_t lowercase_count{};
    size_t uppercase_count{};

    std::cout << "Original string: " << thought << std::endl;

    for (char character : thought) {
        if (std::islower(character)) {
            std::cout << "Lowercase: " << character << std::endl;
            ++lowercase_count;
        }
        if (std::isupper(character)) {
            ++uppercase_count;
        }
    }
    std::cout << "Found " << lowercase_count << " lowercase characters and "
              << uppercase_count << " uppercase characters.\n";

    // ------------------- Check if character is a digit -------------------
    std::cout << "\n=== std::isdigit ===\n";
    char statement[] {"Mr Hamilton owns 221 cows. That's a lot of cows! The kid exclaimed."};
    std::cout << "Statement: " << statement << std::endl;

    size_t digit_count{};
    for (char character : statement) {
        if (std::isdigit(character)) {
            std::cout << "Found digit: " << character << std::endl;
            ++digit_count;
        }
    }
    std::cout << "Total digits found: " << digit_count << "\n";

    // ------------------- Convert to uppercase and lowercase -------------------
    std::cout << "\n=== std::toupper and std::tolower ===\n";
    char original_str[] {"Home. The feeling of belonging"};
    char dest_str[std::size(original_str)];

    // Convert to uppercase
    for (size_t i{}; i < std::size(original_str); ++i) {
        dest_str[i] = std::toupper(original_str[i]);
    }
    std::cout << "Uppercase version: " << dest_str << std::endl;

    // Convert to lowercase
    for (size_t i{}; i < std::size(original_str); ++i) {
        dest_str[i] = std::tolower(original_str[i]);
    }
    std::cout << "Lowercase version: " << dest_str << std::endl;

    return 0;
}
