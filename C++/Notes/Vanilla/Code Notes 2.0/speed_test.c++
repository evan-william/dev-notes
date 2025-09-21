#include <iostream>
#include <chrono>
using namespace std;
using namespace std::chrono;

int main() {
    auto start = high_resolution_clock::now();

    for (unsigned i = 0; i < 10000000; i++) {
        cout << i << endl; 
    }

    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(stop - start); // Cast to milliseconds
    cout << "Execution time: " << duration.count() << " ms" << endl;

    return 0;
}
