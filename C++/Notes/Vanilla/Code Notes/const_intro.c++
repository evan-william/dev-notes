// MAKES STUFF UNCHANGEABLE ONCE SET
#include <iostream>
#include <string>

using namespace std;

int main() {

    // -------------------------------
    // 1. Basic const variable
    // -------------------------------
    const int maxScore = 100;
    cout << "Max Score is: " << maxScore << endl;

    // maxScore = 200; // ❌ Error: Cannot assign to a const variable


    // -------------------------------
    // 2. const with pointers
    // -------------------------------

    int a = 10;
    int b = 20;

    // (a) Pointer to const value (can't change the value)
    const int* ptr1 = &a;
    // *ptr1 = 30; // ❌ Error: value pointed by ptr1 is const
    ptr1 = &b;     // ✅ Okay: pointer itself can change

    // (b) Const pointer (can't change where it points)
    int* const ptr2 = &a;
    *ptr2 = 40;    // ✅ Okay: value pointed can change
    // ptr2 = &b;  // ❌ Error: pointer address can't change

    // (c) Const pointer to const value
    const int* const ptr3 = &a;
    // *ptr3 = 50; // ❌ Error: can't change value
    // ptr3 = &b;  // ❌ Error: can't change address


    // -------------------------------
    // 3. const function parameters
    // -------------------------------
    auto printLength = [](const string& text) {
        // text += " world"; // ❌ Error: text is const
        cout << "Length: " << text.length() << endl;
    };

    string myText = "Hello";
    printLength(myText);


    // -------------------------------
    // 4. const return types and methods
    // -------------------------------
    class Person {
    private:
        string name;
    public:
        Person(const string& name) : name(name) {}

        // const member function: promises not to modify object
        string getName() const {
            return name;
        }

        // Non-const member function: can modify object
        void changeName(const string& newName) {
            name = newName;
        }
    };

    const Person p1("Alice");
    cout << "Name: " << p1.getName() << endl;
    // p1.changeName("Bob"); // ❌ Error: can't call non-const method on const object

    Person p2("Charlie");
    p2.changeName("Dave"); // ✅ Allowed on non-const object
    cout << "Name: " << p2.getName() << endl;


    // -------------------------------
    // 5. const global constant (e.g., PI)
    // -------------------------------
    const double PI = 3.1415926535;
    double radius = 5;
    double area = PI * radius * radius;
    cout << "Area of circle with radius 5 = " << area << endl;


    return 0;
}
