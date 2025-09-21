#include <iostream> // For input/output (cout, cin)
#include <algorithm> // For transform, count, find, reverse, etc.
#include <cctype> // For character checks like toupper, islower
#include <string> // To use the std::string class
#include <sstream> // For splitting strings using getline()
#include <vector> // For list-like operations (like Python lists)

using namespace std;

int main() {
    string str = "hello WORLD";

    // Capitalize (first letter upper, rest lower)
    str[0] = toupper(str[0]);
    for (int i = 1; i < str.length(); i++) str[i] = tolower(str[i]);
    cout << "capitalize: " << str << endl;

    // Lowercase
    transform(str.begin(), str.end(), str.begin(), ::tolower);
    cout << "lower: " << str << endl;

    // Uppercase
    transform(str.begin(), str.end(), str.begin(), ::toupper);
    cout << "upper: " << str << endl;

    // Count character
    int countL = count(str.begin(), str.end(), 'L');
    cout << "count('L'): " << countL << endl;

    // Index of character
    size_t idx = str.find('E');
    cout << "index('E'): " << idx << endl;

    // Find substring
    size_t found = str.find("OR");
    cout << "find('OR'): " << found << endl;

    // Replace '/' with '-'
    string date = "27/11/2022";
    replace(date.begin(), date.end(), '/', '-');
    cout << "replace: " << date << endl;

    // Split string by '/'
    string date2 = "27/11/2022";
    stringstream ss(date2);
    string part;
    cout << "split: ";
    while (getline(ss, part, '/')) {
        cout << part << " ";
    }
    cout << endl;

    // isalnum
    string alphanum = "abc123";
    bool isAlnum = all_of(alphanum.begin(), alphanum.end(), ::isalnum);
    cout << "isalnum: " << boolalpha << isAlnum << endl;

    // isnumeric
    string numeric = "12345";
    bool isNumeric = all_of(numeric.begin(), numeric.end(), ::isdigit);
    cout << "isnumeric: " << isNumeric << endl;

    // Center (manual)
    string word = "Python";
    int width = 10;
    int pad = (width - word.length()) / 2;
    string centered = string(pad, '*') + word + string(width - pad - word.length(), '*');
    cout << "center: " << centered << endl;

    // islower
    string s1 = "hello world";
    bool isLower = all_of(s1.begin(), s1.end(), [](char c){ return !isalpha(c) || islower(c); });
    cout << "islower: " << isLower << endl;

    // isupper
    string s2 = "HELLO WORLD";
    bool isUpper = all_of(s2.begin(), s2.end(), [](char c){ return !isalpha(c) || isupper(c); });
    cout << "isupper: " << isUpper << endl;

    return 0;
}