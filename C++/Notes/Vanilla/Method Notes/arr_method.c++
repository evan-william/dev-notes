#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    vector<string> food = {"burger", "burger", "fries"};

    // Append
    food.push_back("burger");
    cout << "append: ";
    for (auto &f : food) cout << f << " ";
    cout << endl;

    // Clear
    vector<string> temp = food;
    temp.clear();
    cout << "clear: size = " << temp.size() << endl;

    // Count
    int countB = count(food.begin(), food.end(), "burger");
    cout << "count('burger'): " << countB << endl;

    // Copy
    vector<string> copyFood = food;
    cout << "copy: ";
    for (auto &f : copyFood) cout << f << " ";
    cout << endl;

    // Index
    auto it = find(food.begin(), food.end(), "fries");
    if (it != food.end())
        cout << "index('fries'): " << distance(food.begin(), it) << endl;

    // Insert at position 1
    food.insert(food.begin() + 1, "shake");
    cout << "insert: ";
    for (auto &f : food) cout << f << " ";
    cout << endl;

    // Pop at position 3
    food.erase(food.begin() + 3);
    cout << "pop: ";
    for (auto &f : food) cout << f << " ";
    cout << endl;

    // Remove value
    it = find(food.begin(), food.end(), "fries");
    if (it != food.end()) food.erase(it);
    cout << "remove: ";
    for (auto &f : food) cout << f << " ";
    cout << endl;

    // Reverse
    reverse(food.begin(), food.end());
    cout << "reverse: ";
    for (auto &f : food) cout << f << " ";
    cout << endl;

    return 0;
}