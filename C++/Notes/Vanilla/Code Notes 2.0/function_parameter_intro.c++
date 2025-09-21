#include <iostream>

int addNumbers(int first_number, int second_number) {
    int sum = first_number + second_number;
    return sum;
}

int main(){
    int first_number = 12; // THIS IS DEFINE AND CALL FUNCTION
    int second_number = 9;
    int total = addNumbers(first_number, second_number);

    std::cout << "The total1 is: " << total << std::endl;

    // CAN ALSO THESE 2 STEPS
    //1.
    int total2 = addNumbers(34,7);
    
    std::cout << "The total2 is: " << total2 << std::endl;

    //2.
    std::cout << "The total3 is: " << addNumbers(40,300) << std::endl ;

    
}

