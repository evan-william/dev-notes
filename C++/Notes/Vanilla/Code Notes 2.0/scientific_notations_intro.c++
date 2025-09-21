/*
THIS ALLOWS TO DO something liek 1.92e8 
e means = 10 to the power of
so e8 is 10 ^ 8
*/
#include <iostream>
#include <iomanip>

int main(){
    std::cout << std::setprecision(20); // THIS INSTANCE NEED TO BE SET THE COUT CAN SEE PRECISION OF 20 DIGITS

    double number5 {192400023};
    double number6 {1.92400023e8};
    double number7 {1.924e8};           // Can ommit the lower 00023
                                        // for simplicity if our application allows that.
    double number8 {0.00000000003498};
    double number9 {3.498e-11}; // multiply with 10 exp(-11)
    
    std::cout << "number5 is : " << number5 << std::endl;
    std::cout << "number6 is : " << number6 << std::endl;
    std::cout << "number7 is : " << number7 << std::endl;
    std::cout << "number8 is : " << number8 << std::endl;
    std::cout << "number9 is : " << number9 << std::endl;
}