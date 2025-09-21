#include <iostream>

int main(){
    int firstNumber = 12;
    int secondNumber = 9;

    int sum = firstNumber + secondNumber;
    
    std::cout << "The sum is " << sum << std::endl;

    // CAN ALSO STORE DATA LIKE THIS

    int SfirstNumber {12};
    int SsecondNumber {18};

    int sum2 = SfirstNumber + SsecondNumber;
    std::cout << "The sum2 is " << sum2 << std::endl;

    // CAN ALSO STORE THIS

    float dFirstNumber (12.22);
    int dSecondNumber (30);

    float sum3 = dFirstNumber + dSecondNumber;
    std::cout << "The sum3 is " << sum3 << std::endl;


}