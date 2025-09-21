#include <iostream>


int main(){

    // BELOW IS TENARY OPERATIONS
    // condition ? value_if_true : value_if_false;
	int max{};
    
    int a{35};
    int b{200};
	
    std::cout << std::endl;
	std::cout << "using regular if " << std::endl;
	
    /*
    if(a >  b){
        max = a;
    }else{
        max = b;
    }
    */


    // THIS IS TENARY EXPRESSION, ITS result = (condition) ? option1 : option2 ;
    max = (a > b)? a : b; // Ternary operator
    // EQUIVALENT TO 
    /* 
        if (condition) {
            result = option1;
        } else {
            result = option2;
        }
    */
	
    std::cout << "max : " << max << std::endl;
	
    std::cout << std::endl;
    std::cout << "speed" << std::endl;
    bool fast = false;

    int speed {fast ? 300 : 150};

    std::cout << "The speed is " << speed << std::endl;
    
    
    return 0;
}