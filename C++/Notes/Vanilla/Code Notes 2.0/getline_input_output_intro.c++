#include <iostream>
#include <string> // THIS USUALLY NOT NEEDED BUT CAN MAKE STRINGING MORE BETTER AND PORTABLE AND NOT BREAK?

int main(){
    int age;
    std::string name;

    std::cout << "Please type in your name: ";
    // INSTEAD OF just std::cin >> name, use this below, cuz cin only read until it found a white space!!
    std::getline(std::cin, name);

    std::cout << "Please type in your age: ";
    std::cin >> age;

    std::cout << "Hello " << name << " so you are " << age << " years old ?" << std::endl;

    // WE CAN ALSO DO THIS!
    int int2;
    std::string string2;
    std::cout << "Please type a string and int at below: " << std::endl;
    std::cin >> string2 >> int2; // THIS ONE, TAKES 2 INPUT IMMEDIATELY
    std::cout << "Your string is: " << string2 << " Your int is: " << int2 << std::endl;
}

