#include <iostream>


int main(){

	int number1 {75};
    int number2 {60};
    bool result = (number1 < number2);//Expression yielding the condition
    
    /*
	
	std::cout << std::boolalpha << "result : " << result << std::endl; 
	
	std::cout << std::endl;
	std::cout << "free standing if statement" << std::endl;
   
    //if(result){
	if(result == true){
        std::cout << number1 << " is less than " << number2 << std::endl;
    }
    
    //if(!result){
	if(!(result == true)){
        std::cout << number1 << " is NOT less than " << number2 << std::endl;
    }

    */


   	//Using else
    /*
	std::cout << std::endl;
	std::cout << "using the else clause : " << std::endl;
	
	if(result == true){
        std::cout << number1 << " is less than " << number2 << std::endl;
    }else{
        std::cout << number1 << " is NOT less than " << number2 << std::endl;
    }
    */


	//Use expression as condition directly
    /*
	std::cout << std::endl;
	std::cout << "Using expression as condition : " << std::endl;
	
	if(number1 < number2){
        std::cout << number1 << " is less than " << number2 << std::endl;
    }else{
        std::cout << number1 << " is NOT less than " << number2 << std::endl;
    }
    */


	//Nesting if statements
	std::cout << std::endl;
	std::cout << "Nesting if statements" << std::endl;
	
    bool red = false;
    bool green {true};
    bool yellow {false};
    bool police_stop{true};
    
    /*
     *      If green : go
     *      If red, yellow : stop
     *      If green and police_stop : stop
     * */
     /*
     if(red){
         std::cout << "Stop" << std::endl;
     }
     if(yellow){
         std::cout << "Slow down" << std::endl;
     }
	 if(green){
		 std::cout << "Go" << std::endl;
	 }
     */

    /*
    std::cout << std::endl;
	 std::cout << "Police officer stops(verbose)" << std::endl;
	 if(green){
         if(police_stop){
             std::cout << "Stop" << std::endl;
         }
         else{
             std::cout << "Go" << std::endl;
         }

     }
     */


     std::cout << std::endl;
	 std::cout << "Police officer stops(less verbose)" << std::endl;
	 if(green && !police_stop){
         std::cout << "Go" << std::endl;
     }else{
         std::cout << "Stop" << std::endl;
     }


     #include <iostream>


     // Tools
     const int Pen{ 10 }; 
     const int Marker{ 20 };
     const int Eraser{ 30 };
     const int Rectangle{ 40 };
     const int Circle{ 50 };
     const int Ellipse{ 60 };
     
    
         int tool {Ellipse}; // CAN DO EITHER 60 OR Ellipse
     
         if (tool == Pen) {
             std::cout << "Active tool is pen" << std::endl;
             //Do the actual painting
         }
         else if (tool == Marker) {
             std::cout << "Active tool is Marker" << std::endl;
         }
         else if (tool == Eraser) {
             std::cout << "Active tool is Eraser" << std::endl;
         }
         else if (tool == Rectangle) {
             std::cout << "Active tool is Rectangle" << std::endl;
         }
         else if (tool == Circle) {
             std::cout << "Active tool is Circle" << std::endl;
         }
         else if (tool == Ellipse) {
             std::cout << "Active tool is Ellipse" << std::endl;
         }
     
         std::cout << "Moving on" << std::endl;
         
         if (red) {
            std::cout << "Stop" << std::endl;
         }
         if (yellow) {
            std::cout << "Slow Down" << std::endl;
         }
         if (green) {
            std::cout << "Go" << std::endl;
         
    return 0;
}