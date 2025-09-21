// EXIST TRUE OR FALSE ONLY
#include <iostream>


int main(){

    bool red_light {false}; 
    bool green_light{true}; 

    // red_light = true; THIS TO CHANGE THE CODE RED_LIGHT TO TRUE
    
    // CAN CHECK IF TRUE OR FALSE WITH == , BUT DEFAULT IS TRUE SOOO
    if(red_light == true){ 
        std::cout << "Stop!" << std::endl;
    }else {
        std::cout << "Go through!" << std::endl;
    }

    // SO CAN JUST DO THIS, BASICALLY SAME LIKE green_light == true
    if(green_light){
        std::cout << "The light is green!" << std::endl;
    }else{
        std::cout << "The light is NOT green!" << std::endl;
    }

    //sizeof()
    std::cout << "sizeof(bool) : " << sizeof(bool) << std::endl;


    //Printing out a bool
    //1 -->> true
    //0 -->> false
    std::cout << std::endl;
    std::cout << "red_light : " << red_light << std::endl;
    std::cout << "green_light : " << green_light << std::endl;

    std::cout << std::boolalpha; // TO PRINT TRUE OR FALSE ON PROGRAM WITH BOOL
    std::cout << "red_light : " << red_light << std::endl;
    std::cout << "green_light : " << green_light << std::endl;

    std::cout << std::noboolalpha; // TO REVERT BACK
    std::cout << "red_light : " << red_light << std::endl;
    std::cout << "green_light : " << green_light << std::endl;
   
    return 0;
}