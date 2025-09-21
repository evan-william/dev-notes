// ------------------------
// Class Constructors in C++ (with =default keyword)
// ------------------------

// Default constructor will create empty constructor 
#include <iostream>

// Define constant PI for volume calculation
const double PI {3.1415926535897932384626433832795};

// Class definition for Cylinder
class Cylinder {
    public:
        // -------------------------
        // ✅ 1. Default Constructor
        // -------------------------
        // Using "= default" tells the compiler to auto-generate a default constructor.
        // It initializes the member variables using their default values.
        Cylinder() = default;

        // ----------------------------------
        // ✅ 2. Parameterized Constructor
        // ----------------------------------
        // This constructor allows you to set custom values for base_radius and height
        Cylinder(double rad_param, double height_param) {
            base_radius = rad_param;
            height = height_param;
        }

        // -------------------------
        // ✅ 3. Member Function
        // -------------------------
        // Calculates the volume of the cylinder using:
        // Volume = π * r² * h
        double volume() const {
            return PI * base_radius * base_radius * height;
        }

    private:
        // -------------------------
        // ✅ Member Variables
        // -------------------------
        // These get default-initialized to 1.0 unless overridden by constructors
        double base_radius{1.0};
        double height{1.0};
};

// -------------------------
// ✅ MAIN FUNCTION
// -------------------------
int main() {
    // 1️⃣ Using the DEFAULT constructor
    // Because we didn't pass any parameters, it uses Cylinder() = default;
    // Which keeps base_radius and height at their default {1.0}
    Cylinder cylinder1;
    std::cout << "Volume (default constructor): " << cylinder1.volume() << std::endl;

    // 2️⃣ Using the PARAMETERIZED constructor
    // Passing values (10.0, 5.0), so the matching constructor is called
    Cylinder cylinder2(10.0, 5.0);
    std::cout << "Volume (parameterized constructor): " << cylinder2.volume() << std::endl;

    return 0;
}
