#include <iostream>

int main() {

    // Declare array
    char message[5]  {'H','e','l','l','o'};

    // Print out the array through looping
    std::cout << "message : ";
    for (auto c : message) {
        std::cout << c;
    }
    std::cout << std::endl;

    // Change characters in our array
    message[1] = 'a';

    // Print out the modified array
    std::cout << "modified message : ";
    for (auto c : message) {
        std::cout << c;
    }
    std::cout << std::endl;

    // This will probably print garbage after the array
    std::cout << "message (raw output): " << message << std::endl;

    // Null-terminated character array (C-string)
    char message1[] {'H','e','l','l','o','\0'};
    std::cout << "message1 : " << message1 << std::endl;
    std::cout << "sizeof(message1) : " << sizeof(message1) << std::endl;

    // Array without null character
    char message2[6] {'H','e','l','l','o'};
    std::cout << "message2 : " << message2 << std::endl;
    std::cout << "sizeof(message2) : " << sizeof(message2) << std::endl;

    char message3[] {'H','e','l','l','o'};
    std::cout << "message3 : " << message3 << std::endl;
    std::cout << "sizeof(message3) : " << sizeof(message3) << std::endl;

    // String literal
    char message4[] {"Hello"};
    std::cout << "message4 : " << message4 << std::endl;
    std::cout << "sizeof(message4) : " << sizeof(message4) << std::endl;

    // Can't safely print out arrays other than character arrays
    int numbers[] {1,2,3,4,5};
    std::cout << "numbers : " << numbers << std::endl;

    // ARRAY BOUNDS 

	int numbers7[] {1,2,3,4,5,6,7,8,9,0};
	
	//Read beyond bounds : Will read garbage or crash your program
	//std::cout << "numbers[12] : " << numbers[12] << std::endl;

	//Write beyond bounds. The compiler allows it. But you don't own 
	//the memory at index 12, so other programs may modify it and your
	//program may read bogus data at a later time. Or you can even
	//corrupt data used by other parts of your ptogram

	numbers7[129] = 1000;
	std::cout << "numbers[129] : " << numbers7[129] << std::endl;

    std::cout << "Program ending...." << std::endl;

    return 0;
}
