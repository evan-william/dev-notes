#ifndef CYLINDER_H // THIS IS A WAY TO TELL THE PROCESSOR TO RUN THE CODE AT THE BODY IF CONDITION ABOVE IT IS SATISFIED
#define CYLINDER_H // BASICALLY TO GUARD SO THAT IT IS NOT INCLUDED MORE THAN ONCE

#include "constants.h"

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
    Cylinder(double rad_param, double height_param);
        // ALREADY IN C++
    

    // ----------------------
    // Class method to calculate the volume of the cylinder
    // Volume formula = PI * radius^2 * height
    // ----------------------
    double volume();
    // THE REST IS DEFINED AT cylinder.c++

    // ----------------------
    // Getter methods:
    // Used to READ (access) private member variables from outside the class
    // ----------------------
    double get_base_radius();
    // DEFINED AT CPP
    double get_height();
    // DEFINED AT CPP
    // ----------------------
    // Setter methods:
    // Used to WRITE (modify) private member variables from outside the class
    // ----------------------
    void set_base_radius(double rad_param);
    // DEFINED AT CPP
    void set_height(double height_param);
    // DEFINED AT CPP
        // Sets height to new value
};

#endif