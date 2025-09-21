// 1. Change From Int To Str
/*
string strYear = to_string(year);
*/

// 2. Initialize a Dynamic Array
/*
#include <vector>
vector<char> Tempo;
*/

// 3. Iterates Like for Each
/*
for (char digit : strYear) -> for digit in strYear (IN PYTHON)
*/

// 4. Appending to Array
/*
Tempo.push_back(digit); -> UTILIZE push_back(ANYTHING)
*/

// 5. Finding Stuff in array (THE EXAMPLE IS LIKE PYTHON: if each not in Tempo) 
// if digit not found from begin to end, it will return Tempo.end.
// if digit found , it will ask, is the founded digit != Tempo? , if yes run the function inside it
/*
    #include <algorithm>
    if (find(Tempo.begin(), Tempo.end(), digit) != Tempo.end())
*/ 

// 6. Capitalization first letter
/*
    word[0] = toupper(word[0]);
*/

// 7. len method
/*
    int size_of_Both = line1.size();
*/

// 8. pairing vector from 2 array and reasigning 
/*
    vector<pair<int, int>> combined; 

    for (int y = 0; y < dragonStrength.size(); y ++) {
            combined.push_back({dragonStrength[y], bonus[y]});
        } 

// THIS BELOW ONLY IF WANNA CHECK AND PRINT IT
=======================================================================
    for (auto each : combined) {
          cout << "(" << each.first << ", " << each.second << ")" << endl;
      }
========================================================================

    sort(combined.begin(), combined.end()); // THIS IS EXTRA, ONLY IF U WANNA SORT BASED ON THE FIRST ELEMENT

    for (auto& p : combined) {
            dragonStrength.push_back(p.first);
            bonus.push_back(p.second);
        }
*/

// 9. Delete everything in an array
/*
    ArrayName.clear()
*/

// 10. Input like 1 2 7 5 8 (5 Things) to Array
/*
    int TvOnSale;
    int CarryCapacity;

    cin >> TvOnSale >> CarryCapacity;

    vector<int> Price(TvOnSale);
    
    for(int x = 0; x < TvOnSale ; x ++) {
        cin >> Price[x];   -> cin it all
    }

    sort(Price.begin(), Price.end()); This to sort it , OPTIONAL
*/

// 11. Sort on vector, ASC DESC
/*
    #include <vector>
    #include <algorithm>
    ASC:
    sort(Price.begin(), Price.end());
    DESC:
    sort(Price.begin(), Price.end(), greater<int>())
*/

// 12. Find Sum of an array vector
/*
    #include <numeric>
    int total = accumulate(numbers.begin(), numbers.end(), 0);

    0 is the initial value of the sum
*/

// 13. Input Line
/*
    #include <string>
    std::getline(std::cin, name);
*/

// 14. Exit Program
/*
    #include <cstdlib>
    exit(0);
*/

// 15. If array empty (CHECKING)
/*
    if (bookList.empty())
*/

// 16. Delete things in array
/*
    bookList.erase(bookList.begin() + index - 1);
*/

// 17. Random Randint
/*
    #include <cstdlib>  // for rand()
    #include <ctime>    // for time()

    srand(time(0));  // Seed once!
    int randomNumber = rand() % 10 + 1;  // From 1 to 10
*/

// 18. Directly read into vector without making a copy
/*
    for (const auto name : list)
*/

// 19. Clear Screen
/*
    #include <cstdlib>
    void clearScreen() {
        #ifdef _WIN32
            system("cls");
        #else
            system("clear");
        #endif
    }
*/

// 20. To Lower a Line
/*
    #include <string>
    
    getline(cin,choice)
    transform(choice.begin(), choice.end(), choice.begin(), ::tolower);
*/

// 21. Common trick in C++ to convert a character like '1' into the integer 1
/*
    char digitChar = '7';
    int digit = digitChar - '0'; // digit becomes 7
*/

// 22. Stack Method
/*
    void compute(const vector<int>& ln) {
    vector<int> stack;

    for (int num : ln) {
        if (!stack.empty() && stack.back() != num) {
            stack.pop_back(); 
        } else {
            stack.push_back(num);
        }
    }

    cout << stack.size() << endl;
}
*/