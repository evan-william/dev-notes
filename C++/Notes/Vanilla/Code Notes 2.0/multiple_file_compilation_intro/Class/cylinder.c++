#include "cylinder.h"

Cylinder::Cylinder (double rad_param, double height_param) {
    base_radius = rad_param;
    height = height_param;
}

double Cylinder::volume(){ // THIS WILL TELL COMPILER THIS IS IMPLEMENTATION OF A FUNCTION WE HAVE IN CLASS AND RETURN TYPE IS INFRONT 
    // THIS TELLS OUR FUNCTION CALLED VOLUME LIVES IN THE CYLINDER CLASS
    return PI * base_radius * base_radius * height;
}

 // ----------------------
    // Getter methods:
    // Used to READ (access) private member variables from outside the class
    // ----------------------
double Cylinder::get_base_radius() {
    return base_radius; // Returns the current value of base_radius
}

double Cylinder::get_height() {
    return height; // Returns the current value of height
}

    // ----------------------
    // Setter methods:
    // Used to WRITE (modify) private member variables from outside the class
    // ----------------------
void Cylinder::set_base_radius(double rad_param) {
    base_radius = rad_param; // Sets base_radius to new value
}

void Cylinder::set_height(double height_param) {
    height = height_param; // Sets height to new value
}