#include <iostream>


int main(){
   
   //Addition
   int number1{2};
   int number2{7};

   int result = number1 + number2;
   std::cout << "result : " << result << std::endl;

    //Subtraction
    result = number2 - number1 ;
   std::cout << "result : " << result << std::endl;

   result = number1 - number2;
   std::cout << "result : " << result << std::endl;

   //Multiplication
   result = number1 * number2;
   std::cout << "result : " << result << std::endl;


   //Division
   result = number2 / number1;
   std::cout << "result : " << result << std::endl;


   //Modulus
   result = number2 % number1; // 7 % 2
   std::cout << "result : " << result << std::endl; // 1

   result = 31 % 10;
   std::cout << "result : " << result << std::endl; // 1

   //PREDESENCE AND ASSOSIATION (MULTIPLE OPERATION)
   /*
   1. theres operation to go from left to right
   2. and right to left
   */
   int a {6};
   int b {3};
   int c {8};
   int d {9};
   int e {3};
   int f {2};
   int g {5};
        
   int result2 = a + b * c -d/e -f + g; //  6 +  24  -   3 - 2 + 5
    
   std::cout << "result2 : " << result2 << std::endl;

   result2 = a/b*c +d - e + f;  //   16 + 9 - 3 + 2
   std::cout << "result2 : " << result2 << std::endl;

   result2 = (a + b) * c -d/e -f + g; // 72-3-2+5
   std::cout << "result2 : " << result2 << std::endl;


   // COMPOUND OPERATOR
    
   int value {45};
    
   std::cout << "The value is : " << value << std::endl;
    
   std::cout << std::endl;
   value = value + 5;
    //value +=5; // equivalent to value = value + 5
   std::cout << "The value is (after +=5) : " << value << std::endl; // 50

   std::cout << std::endl;
   value -=5; // equivalent to value = value - 5
   std::cout << "The value is (after -=5) : " << value << std::endl; // 45 

   std::cout << std::endl;
   value *=2;
   std::cout << "The value is (after *=2) : " << value << std::endl; // 90

   std::cout << std::endl;
   value /= 3;
   std::cout << "The value is (after /=3) : " << value << std::endl; // 30

   std::cout << std::endl;
   value %= 11;
   std::cout << "The value is (after %=11) : " << value << std::endl;// 8

    // RELATIONAL OPERATOR
   int number3 {20};
   int number4 {20};
	
    std::cout << "number3 : " << number3 << std::endl;
    std::cout << "number4 : " << number4 << std::endl;
	
	std::cout << std::endl;
	std::cout << "Comparing variables" << std::endl;
	
    std::cout << std::boolalpha ; // Make bool show up as true/false instead of 1/0
	//Stress the need for parentheses here
    std::cout << "number3 < number4 : " << (number3 < number4) << std::endl;
	std::cout << "number3 <= number4 : " << (number3 <= number4) << std::endl;
    std::cout << "number3 > number4 : " << (number3 > number4) << std::endl;
    std::cout << "number3 >= number4 : " << (number3 >= number4) << std::endl;
    std::cout << "number3 == number4 : " << (number3 == number4) << std::endl;
    std::cout << "number3 != number4 : " << (number3 != number4) << std::endl;

	std::cout << std::endl;
	std::cout << "store comparison result and use it later" << std::endl;
	
	bool result3 = (number3 == number4);
    
    std::cout <<  number3 << " == " << number4 << " : " << result3 <<  std::endl;

    return 0;
} 