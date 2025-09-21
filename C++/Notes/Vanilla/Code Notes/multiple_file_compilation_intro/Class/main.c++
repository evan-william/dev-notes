#include <iostream> // For std::cout and std::endl
// #include "constants.h" THIS NO NEED TO BE DEFINED AGAIN CUZ ITS ALREADY IN cylinder.h BUT LOOK BELOW
#include "cylinder.h"
#include "cylinder.h"
#include "cylinder.h" // THIS NOW WILL WORK FINE CUZ WE ALREADY PUT GUARD 

// Define a constant value of PI to be used in volume calculation
// ALREADY DEFINED AT constant.h

// ----------------------------
// Definition of the Cylinder class
// ----------------------------
// ALREADY DEFINED AT cylinder.h

// ----------------------------
// Main function
// Entry point of the program
// ----------------------------
int main() {
    // STEP 1: Create a Cylinder object with specific radius and height
    // This calls the parameterized constructor: Cylinder(double, double)
    Cylinder cylinder1(10, 10);

    // STEP 2: Calculate and print the volume
    std::cout << "Volume (initial): " << cylinder1.volume() << std::endl;

    // STEP 3: Modify the cylinder's radius and height using SETTER methods
    // These are safe ways to modify private variables
    cylinder1.set_base_radius(100); // Change radius to 100
    cylinder1.set_height(10);       // Change height to 10

    // STEP 4: Recalculate and print the new volume after modification
    std::cout << "Volume (after modification): " << cylinder1.volume() << std::endl;

    return 0; // Exit the program
}
