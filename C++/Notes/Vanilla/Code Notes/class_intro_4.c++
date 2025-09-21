// -------------------------------------------
// Class Destructors in C++ with Heap Concepts
// -------------------------------------------

#include <iostream>
#include <string_view> // For efficient string passing without copying

// -----------------------------
// Definition of the Dog class
// -----------------------------
class Dog {
public:
    // Default constructor (does nothing special, but provided here explicitly)
    Dog() = default;

    // Custom constructor that receives parameters
    Dog(std::string_view name_param, std::string_view breed_param, int age_param);

    // Destructor: gets called automatically when an object is destroyed
    ~Dog();

private:
    std::string name;   // Name of the dog
    std::string breed;  // Breed of the dog
    int* p_age{nullptr}; // Pointer to int for storing age dynamically (on the heap)
};


// ------------------------------------------------------------
// Constructor Implementation (outside the class definition)
// ------------------------------------------------------------
// Why use Dog::Dog? Because we're implementing the constructor declared inside the class.
// This tells the compiler: "This is the constructor of the Dog class"
// Doing it outside the class improves code readability and separation of declaration/definition
Dog::Dog(std::string_view name_param, std::string_view breed_param, int age_param) {
    // Assign values to name and breed (stack variables, managed automatically)
    name = name_param;
    breed = breed_param;

    // ----------------------------------------
    // Dynamic Memory Allocation using 'new'
    // ----------------------------------------
    // Here we allocate memory for an integer on the HEAP (not the stack)
    // This allows the data (age) to live independently of the function scope
    p_age = new int;     // Allocates memory for ONE int on the heap
    *p_age = age_param;  // Stores the passed-in age into the allocated heap memory

    std::cout << "Dog constructor called for " << name << std::endl;
}


// ------------------------------------------------------------
// Destructor Implementation (outside the class definition)
// ------------------------------------------------------------
// This will be called when the Dog object is destroyed
// It's our responsibility to clean up dynamically allocated memory (heap)
// If we don't do this, the memory will stay allocated forever — MEMORY LEAK!
Dog::~Dog() { // Gets called automatically when deleted
    delete p_age; // Frees the memory that was allocated with 'new'

    std::cout << "Dog destructor called for : " << name << std::endl;
}


// ------------------------------------------------------------
// This function demonstrates dynamic allocation
// ------------------------------------------------------------
void some_func() {
    // ------------------------------------------
    // Create a Dog object dynamically on the HEAP
    // ------------------------------------------
    // The 'new' keyword allocates memory for the object on the heap
    Dog* p_dog = new Dog("Fluffy", "Shepherd", 2);
    std::cout << "Test" << std::endl;

    // Without 'delete', this object will remain in memory
    // even after this function ends — MEMORY LEAK!
    delete p_dog; // Calls the destructor and releases memory
}


// ------------------------------------------------------------
// Main function
// ------------------------------------------------------------
int main() {
    some_func(); // Creates and deletes a Dog object properly

    std::cout << "Done!" << std::endl;
    return 0;
    
    /* Explanation
    Dog::Dog(...) -> Constructor implemented outside class with Dog:: scope resolution
    new	-> Allocates memory dynamically on the heap
    delete -> Releases memory allocated with new
    Heap ->	Memory region for dynamic lifetime management
    Destructor -> Cleans up heap memory; prevents leaks
    p_age = new int; -> Allocates memory for age
    delete p_age; ->	Destructor cleans up p_age
    */
}
