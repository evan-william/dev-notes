#include <iostream>
#include <string_view> // Required for std::string_view (efficient read-only string type)

// THIS POINTER EXPLANATION
class Dog {
public:
    Dog() = default; // Default constructor (not used here but good to have)
    
    // Custom constructor
    Dog(std::string_view name_param, std::string_view breed_param, int age_param);
    
    // Destructor to clean up dynamic memory
    ~Dog();

    // Method to print dog info
    void print_info() {
        std::cout << "Dog (" << this << ") : [ name : " << name
                  << " breed : " << breed << " age : " << *p_age << "]" << std::endl;
    }

    // Chained setters using REFERENCES (so we can use . instead of ->)
    
    Dog& set_dog_name(std::string_view name) {
        this->name = name; // 'this' is a pointer to the current object, so 'this->name'
        return *this;      // return a reference to the current object
    }

    Dog& set_dog_breed(std::string_view breed) {
        this->breed = breed;
        return *this;
    }

    Dog& set_dog_age(int age) {
        *(this->p_age) = age; // p_age is a pointer, so we dereference it
        return *this;
    }

    // BELOW IF THE POINTER VERSION
    /*
    Dog* set_dog_name(std::string_view name) {
        this->name = name;
        return this;  // 'this' is already a pointer
    }

    Dog* set_dog_breed(std::string_view breed) {
        this->breed = breed;
        return this;
    }

    Dog* set_dog_age(int age) {
        *(this->p_age) = age;
        return this;
    }

    USAGE:
    dog1.set_dog_name("Pumba")->set_dog_breed("Wire Fox Terrier")->set_dog_age(4);
    */

    // BELOW IS WITHOUT BOTH 
    /*
    void set_dog_name(std::string_view name) {
    this->name = name;
    }

    void set_dog_breed(std::string_view breed) {
        this->breed = breed;
    }

    void set_dog_age(int age) {
        *(this->p_age) = age;
    )

    USAGE:
    dog1.set_dog_name("Pumba");
    dog1.set_dog_breed("Wire Fox Terrier");
    dog1.set_dog_age(4);
    */

private:
    std::string name;
    std::string breed;
    int* p_age{nullptr}; // Will point to dynamic memory on the heap
};

// Constructor implementation (outside the class using Dog::)
Dog::Dog(std::string_view name_param, std::string_view breed_param, int age_param) {
    name = name_param;
    breed = breed_param;

    p_age = new int;       // Dynamic memory allocation on heap
    *p_age = age_param;    // Store the passed age

    std::cout << "Dog constructor called for " << name << " at " << this << std::endl;
}

// Destructor implementation
Dog::~Dog() {
    delete p_age; // Clean up dynamically allocated memory
    std::cout << "Dog destructor called for " << name << " at " << this << std::endl;
}

// ----------------------
// Main Program
// ----------------------
int main() {
    Dog dog1("Fluffy", "Shepherd", 2); // Constructor called

    dog1.print_info(); // Prints current info

    // Chained calls to update name, breed, and age
    dog1.set_dog_name("Pumba")
        .set_dog_breed("Wire Fox Terrier")
        .set_dog_age(4);

    dog1.print_info(); // Check updated info

    std::cout << "Done!" << std::endl;
    return 0; // Destructor automatically called here when dog1 goes out of scope
}
