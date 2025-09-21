#include <iostream>
#include <string_view>

// CONSTRUCT AND DECONSTRUCT ORDER 

// ----------------------
// Dog class declaration 
// ----------------------
class Dog {
public:
    Dog() = default; // Default constructor
    Dog(std::string_view name_param, std::string_view breed_param, int age_param); // Custom constructor
    ~Dog(); // Destructor (automatically called at the end of lifetime)

private:
    std::string name;
    std::string breed;
    int* p_age{nullptr}; // Pointer to dynamically allocated memory (on the heap)
};

// ----------------------
// Constructor Definition
// ----------------------
Dog::Dog(std::string_view name_param, std::string_view breed_param, int age_param) {
    name = name_param;
    breed = breed_param;

    p_age = new int;     // Allocate memory on heap
    *p_age = age_param;  // Store the age

    std::cout << "Dog constructor called for " << name << std::endl;
}

// ----------------------
// Destructor Definition
// ----------------------
Dog::~Dog() {
    delete p_age; // Free the heap memory (very important!)
    std::cout << "Dog destructor called for : " << name << std::endl;
}

// ----------------------
// Main Function
// ----------------------
int main() {
    Dog dog1("Dogyy1", "Shepherd", 2);
    Dog dog2("Dogyy2", "Shepherd", 3);
    Dog dog3("Dogyy3", "Shepherd", 5);
    Dog dog4("Dogyy4", "Shepherd", 1);

    return 0; // ← Here's the secret: Destructors get called **here** automatically!
}
