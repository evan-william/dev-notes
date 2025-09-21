#include <iostream>

int main() {
	// How we've used pointers so far
	int number {22}; // Stack
	int* p_number = &number;

	std::cout << std::endl;
	std::cout << "Declaring pointer and assigning address : " << std::endl;
	std::cout << "number : " << number << std::endl;
	std::cout << "p_number : " << p_number << std::endl;
	std::cout << "&number : " << &number << std::endl;
	std::cout << "*p_number : " << *p_number << std::endl;

	int* p_number1; // Uninitialized pointer, contains junk address
	int number1 {12};
	p_number1 = &number1; // Make it point to a valid address
	std::cout << std::endl;
	std::cout << "Uninitialized pointer : " << std::endl;
	std::cout << "*p_number1 : " << *p_number1 << std::endl;

	// BAD: Writing into uninitialized pointer through dereference
	/*
	int* p_number2; // Contains junk address
	std::cout << "Writting in the 55" << std::endl;
	*p_number2 = 55; // Writing into junk address: BAD!
	std::cout << std::endl;
	std::cout << "Writing into uninitialized pointer through dereference" << std::endl;
	std::cout << "p_number2 : " << p_number2 << std::endl;
	std::cout << "*p_number2 : " << *p_number2 << std::endl;
	*/

	// Initializing pointer to null
	int* p_number3 {}; // Initialized with nullptr
	std::cout << "Writting into nullptr memory (commented out to avoid crash)" << std::endl;
	// *p_number3 = 33; // BAD: crash
	std::cout << "Done writting" << std::endl;

	std::cout << std::endl;
	std::cout << "Reading and writing through nullptr (commented out to avoid crash)" << std::endl;
	// std::cout << "p_number3 : " << p_number3 << std::endl;
	// std::cout << "*p_number3 : " << *p_number3 << std::endl;

	// Dynamic heap memory
	int* p_number4 {nullptr};
	p_number4 = new int; // Dynamically allocate memory
	*p_number4 = 77;     // Write to it

	std::cout << std::endl;
	std::cout << "Dynamically allocating memory : " << std::endl;
	std::cout << "*p_number4 : " << *p_number4 << std::endl;


    // DIFF BETWEEN HEAP AND STACk = https://chatgpt.com/c/68170141-ce38-800d-b7b8-67a323c2c829
	delete p_number4;
	p_number4 = nullptr; // ALWAYS RESET THE POINTER AFTER DELETE, THIS WILL MAKE LIFE A WHOLE LOT EASIER

	// Initialize with valid memory address at declaration
	int* p_number5 { new int }; // Uninitialized value (junk)
	int* p_number6 { new int(22) }; // Direct initialization
	int* p_number7 { new int{23} }; // Uniform initialization

	std::cout << std::endl;
	std::cout << "Initialize with valid memory address at declaration : " << std::endl;
	std::cout << "p_number5 : " << p_number5 << std::endl;
	std::cout << "*p_number5 : " << *p_number5 << std::endl;

	std::cout << "p_number6 : " << p_number6 << std::endl;
	std::cout << "*p_number6 : " << *p_number6 << std::endl;

	std::cout << "p_number7 : " << p_number7 << std::endl;
	std::cout << "*p_number7 : " << *p_number7 << std::endl;

	// Remember to release memory
	delete p_number5;
	p_number5 = nullptr;

	delete p_number6;
	p_number6 = nullptr;

	delete p_number7;
	p_number7 = nullptr;

	// Can reuse pointer
	p_number5 = new int(81);
	std::cout << "*p_number5 : " << *p_number5 << std::endl;
	delete p_number5;
	p_number5 = nullptr;

	// Calling delete twice: BAD! Will crash or cause uPndefined behavior
	p_number5 = new int(99);
	std::cout << "*p_number5 : " << *p_number5 << std::endl;
	delete p_number5;
	// delete p_number5; // <--- BAD: already deleted! Commented out.P

	std::cout << "Program is ending well" << std::endl;
	return 0;
}
