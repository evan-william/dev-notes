#include <iostream> // For std::cout and std::endl

// Define a constant value of PI to be used in volume calculation
const double PI {3.1415926535897932384626433832795};

// ----------------------------
// Definition of the Cylinder class
// ----------------------------
class Cylinder {

    // ----------------------
    // Private section:
    // These members can ONLY be accessed or modified from inside the class (or via public methods)
    // ----------------------
private:
    double base_radius{1}; // Default value for base radius
    double height{1};      // Default value for height

    // ----------------------
    // Public section:
    // These members can be accessed from outside the class
    // ----------------------
public:

    // 1. Default constructor
    // Compiler will automatically generate a default constructor
    // This allows you to create an object like: Cylinder c;
    Cylinder() = default;

    // 2. Parameterized constructor
    // This constructor allows you to create an object with specific values
    // Example: Cylinder c(10, 5); will set base_radius = 10 and height = 5
    Cylinder(double rad_param, double height_param) {
        base_radius = rad_param;
        height = height_param;
    }

    // ----------------------
    // Class method to calculate the volume of the cylinder
    // Volume formula = PI * radius^2 * height
    // ----------------------
    double volume() {
        return PI * base_radius * base_radius * height;
    }

    // ----------------------
    // Getter methods:
    // Used to READ (access) private member variables from outside the class
    // ----------------------
    double get_base_radius() {
        return base_radius; // Returns the current value of base_radius
    }

    double get_height() {
        return height; // Returns the current value of height
    }

    // ----------------------
    // Setter methods:
    // Used to WRITE (modify) private member variables from outside the class
    // ----------------------
    void set_base_radius(double rad_param) {
        base_radius = rad_param; // Sets base_radius to new value
    }

    void set_height(double height_param) {
        height = height_param; // Sets height to new value
    }
};

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
