// THIS CAN MUCH SHORTEN THE CODE!!! SO WE DONT HAVE TO WRITE std:: EVERY TIME
#include <iostream>
#include <string>

using namespace std;

int main() {
    string name;  
    cout << "Name: ";
    getline(cin, name);
}

// CAN SEE, NOT NEEDED ANY std::cout, std::string, etc etc
// BUT CAN ALSO FILTER IT LIKE BELOW

#include <iostream>
#include <string>

using std::string;

int main() {
    string name;   // ✅ OK
    std::cout << "Name: ";  // ❌ Still need std:: here
    std::getline(std::cin, name);  // ❌ Still need std:: here
}
