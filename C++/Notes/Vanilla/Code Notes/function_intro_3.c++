#include <iostream>
#include <string>
#include <string_view>

// ==========================================
// 1. INPUT & OUTPUT PARAMETER FUNCTIONS
// ==========================================

// Compare two strings and return the larger one via output reference
void max_str(const std::string& input1, const std::string input2, std::string& output) {
    if (input1 > input2) {
        output = input1;
    } else {
        output = input2;
    }
}

// Compare two integers and return the larger one via output reference
void max_int(int input1, int input2, int& output) {
    if (input1 > input2) {
        output = input1;
    } else {
        output = input2;
    }
}

// Compare two doubles and return the larger one via output pointer
void max_double(double input1, double input2, double* output) {
    if (input1 > input2) {
        *output = input1;
    } else {
        *output = input2;
    }
}

// ==========================================
// 2. RETURN VALUE FUNCTIONS
// ==========================================

// Returns the sum of two integers
int sum(int a, int b) {
    int result = a + b;
    std::cout << "In : &result(int) :  " << &result << std::endl;
    return result;
}

// Returns the concatenation of two strings
std::string add_strings(std::string str1, std::string str2) {
    std::string result = str1 + str2;
    std::cout << "In : &result(std::string) :  " << &result << std::endl;
    return result;
}

// ==========================================
// 3. FUNCTION OVERLOADING
// ==========================================

int max(int a, int b) {
    std::cout << "int overload called" << std::endl;
    return (a > b) ? a : b;
}

double max(double a, double b) {
    std::cout << "double overload called" << std::endl;
    return (a > b) ? a : b;
}

double max(int a, double b) {
    std::cout << "(int,double) overload called" << std::endl;
    return (a > b) ? a : b;
}

double max(double a, int b) {
    std::cout << "(double,int) overload called" << std::endl;
    return (a > b) ? a : b;
}

double max(double a, int b, int c) {
    std::cout << "(double,int,int) overload called" << std::endl;
    return a;
}

std::string_view max(std::string_view a, std::string_view b) {
    std::cout << "(string_view,string_view) overload called" << std::endl;
    return (a > b) ? a : b;
}

// ==========================================
// MAIN FUNCTION (Part 1): Demonstrates I/O params and return values
// ==========================================
int main() {
    // 1. Testing max_str (string comparison with output reference)
    std::string out_str;
    std::string string1("Cassablanca");
    std::string string2("Bellevue");

    max_str(string1, string2, out_str);
    std::cout << "max_str : " << out_str << std::endl;

    // 2. Testing max_int (integer comparison with output reference)
    int out_int;
    int in1{45};
    int in2{723};
    max_int(in1, in2, out_int);
    std::cout << "max_int : " << out_int << std::endl;

    // 3. Testing max_double (double comparison with output pointer)
    double out_double;
    double in_double1{45.8};
    double in_double2{76.9};
    max_double(in_double1, in_double2, &out_double);
    std::cout << "max_double : " << out_double << std::endl;

    // 4. Testing return by value functions
    int x{15};
    int y{9};
    int result = sum(x, y);
    std::cout << "Out : &result(int) :  " << &result << std::endl;
    std::cout << "result : " << result << std::endl;

    std::string in_str1{"Hello"};
    std::string in_str2{" World!"};
    std::string result_str = add_strings(in_str1, in_str2);
    std::cout << "Out : &result_str(std::string) :  " << &result_str << std::endl;
    std::cout << "result_str : " << result_str << std::endl;

    // 5. Function overloading examples
    int a = 4, b = 9;
    double da = 5.4, db = 7.4;

    auto r1 = max(da, a, b);               // Calls (double, int, int)
    std::cout << "max(da, a, b): " << r1 << std::endl;

    auto r2 = max("Hello", "World");       // Calls (string_view, string_view)
    std::cout << "max(\"Hello\", \"World\"): " << r2 << std::endl;

    return 0;

    // FUNC OVERLOAD MORE NOTES:
    /*
    Yes — function overloading in C++ means you can define multiple functions with the same name, as long as they differ in their parameter list.

    That difference can be based on:

    ✅ Different number of parameters
    int add(int a, int b);
    int add(int a, int b, int c);
    ✅ Different types of parameters
    double max(double a, double b);
    int max(int a, int b);
    ✅ Different parameter type order
    double max(int a, double b);
    double max(double a, int b);
    */
}
