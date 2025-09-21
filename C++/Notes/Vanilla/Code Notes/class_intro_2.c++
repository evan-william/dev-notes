// ------------------------
// Class Constructors in C++
// ------------------------

/*
    Constructor:
    - Special function inside a class
    - Same name as the class
    - No return type (not even void)
    - Automatically called when an object is created
    - Used to initialize member variables
*/

#include <iostream>

// Define constant PI for volume calculation
const double PI {3.1415926535897932384626433832795};

// Cylinder class definition
class Cylinder {
    // Private member variables (cannot be accessed directly from outside)
    private:
        double base_radius{1.0}; // default radius
        double height{1.0};      // default height

    // Public constructors and methods
    public:

        // 1. Default constructor (no parameters)
        // This gets called when we create an object with no arguments
        Cylinder() {
            base_radius = 2.0;
            height = 2.0;
            // Sets default radius and height to 2.0
        }

        // 2. Parameterized constructor
        // This gets called when we create an object with radius and height
        Cylinder(double rad_param, double height_param) {
            base_radius = rad_param;
            height = height_param;
            // Sets radius and height to the values passed by the user
        }

        // Method to calculate the volume of the cylinder
        double volume() {
            // Volume = π * r² * h
            return PI * base_radius * base_radius * height;
        }
};

// Main function
int main() {
    // Create object using default constructor
    // Calls Cylinder() constructor
    Cylinder cylinder1;

    // Output the volume of the cylinder
    std::cout << "Volume (default constructor): " << cylinder1.volume() << std::endl;

    // Create object using parameterized constructor
    // Calls Cylinder(double, double) constructor
    Cylinder cylinder2(10.0, 5.0);
    std::cout << "Volume (parameterized constructor): " << cylinder2.volume() << std::endl;

    // DEFAULTED CONSTRACTOR TO SET DEFAULT EMPTY CONSTRACTOR
    
    return 0;
}
