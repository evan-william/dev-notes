#include <iostream>

int main(){

    /*
   for( unsigned int i{0} ; i < 10000 ;++i){
       //Whatever we want the loop to run
       std::cout << i <<  " : I love C++" << std::endl;
   }
   std::cout << "Loop done!" << std::endl;
   */

  //Use size_t : a representation of some unsigned int for positive numbers [sizes]
  /*
  for(size_t i{0} ; i < 10 ; ++i){
      std::cout << i << " : I love C++" << std::endl;
  }
  std::cout << "Loop done!" << std::endl;
  */
    /*
    //sizeof(size_t)
    std::cout << "sizeof(size_t) : " << sizeof(size_t) << std::endl;
    */


    //Scope of the iterator
    /*
    for(size_t i{0} ; i < 10 ; ++i){
        std::cout << i << " : I love C++" << std::endl;
    }
    std::cout << "Loop done!" << std::endl;
    // std::cout << "i : " << i << std::endl;Compiler error : i is not in scope
    */


   //Iterator declared outside the loop
   /*
    size_t i{0}; // Iterator defined outside

    for(i ; i < 10 ; ++i){
        std::cout << i << " : I love C++" << std::endl;
    }
    std::cout << "Loop done!" << std::endl;
    std::cout << "i : " << i << std::endl;
    */


    //Leave out the iterator declaration part
    /*
    size_t i{0}; // Iterator defined outside

    for(  ; i < 10 ; ++i){
        std::cout << i << " : I love C++" << std::endl;
    }
    std::cout << "Loop done!" << std::endl;
    std::cout << "i : " << i << std::endl;
    */


   //Don't hard code values : BAD!

    const size_t COUNT{1000};

    for(size_t i{0} ; i < COUNT ; ++i){
        std::cout << i << " : I love C++" << std::endl;
    }
    std::cout << "Loop done!" << std::endl;
   
    // MULTIPLE DECLARATION
    for (size_t i{0} , x {5}, y{22} ; y > 15 ; ++i , x+=5 , y-=1){
        std::cout << "i: " << i << ", x : " << x << ", y : " << y << std::endl;

    }
   
    //Auto type deduction
	for (auto value : {1,2,3,4,5,6,7,8,9,20}){
        //value holds a copy of the current iteration in the whole bag
        std::cout << " value : " << value << std::endl;
    }

    //The comma operator combines
    //two or more  expressions into a single expression,
    // where the value of the operation is the value of its right operand
    
    int increment {5};
    int number10 {10};
    int number20 {20};
    int number30 {25};
    int result = (number10 *= ++increment, number20 - (++increment), number30 += ++increment);
    std::cout << "number1 : " << number10 << std::endl; // 60
    std::cout << "number2 : " << number20 << std::endl; // 20
    std::cout << "number3 : " << number30 << std::endl; // 33
    std::cout << "result : " <<  result << std::endl; // 33

    // WHILE VERSION
    const size_t COUNT3{100};
    size_t i{0}; // Iterator declaration

    while(i < COUNT3 ){ // Test
       std::cout << i << " : I love C++" << std::endl;

       ++i; // Incrementation 
    }
    std::cout << "Loop done!" << std::endl;
   

    // DO WHILE VERSION 

    const int COUNT2{10};
    size_t x{0}; // Iterator declaration

    do{
        std::cout << x << " : I love C++ 2" << std::endl;
        ++x; // Incrementation
    }while( x < COUNT2);

    std::cout << "Loop done!" << std::endl;
}