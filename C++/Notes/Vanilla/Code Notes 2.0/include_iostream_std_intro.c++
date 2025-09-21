#include <iostream> // TO LOAD LIBRARY FOR STD COUT CIN 
// STARTING POINT OF CPP PROGRAM

int main() { 
    std::cout << "Hello World" << std::endl; // endl will print a new line
    // CAN ALSO DO std
    // std::cout << "Number 1";
    // std::cout << "Number 2";
    int test = 7;
    std::cout << "Test Num: " << test << std::endl;

    // ALL STD THINGS:
    /* 
    std::cout (Print data to console)
    std::cin   (Reading data from terminal)
    std::cerr (Printing error to console)
    std::clog (Printing Log messages to console)
    */

    //ERROR
    std::cerr << "std::cerr output : Something went wrong!" << std::endl;

    //LOG MSG
    std::clog << "std::clog output : This is a log message" << std::endl;
}
 