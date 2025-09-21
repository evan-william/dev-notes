#include <iostream>
#include <thread>    // For sleep_for
#include <chrono>    // For milliseconds
#include <string>

using namespace std;

// Function to display text with slow typing effect
void typeText(const string& text, int delayMs = 30) {
    for (char c : text) {
        cout << c << flush;  // flush ensures it's displayed immediately
        this_thread::sleep_for(chrono::milliseconds(delayMs));
    }
}

// Function to display a progress bar
void drawProgressBar(int current, int max, int width = 20) {
    // Calculate fill width based on percentage
    int filledWidth = static_cast<int>(static_cast<double>(current) / max * width);
    
    cout << "[";
    for (int i = 0; i < width; i++) {
        if (i < filledWidth) {
            cout << "=";
        } else {
            cout << " ";
        }
    }
    cout << "] " << current << "/" << max << endl;
}

int main() {
    // Demo the slow-typing text animation
    cout << "Demonstration of slow-typing text effect:" << endl;
    typeText("Hello adventurer! Welcome to the terminal RPG demo.\n", 50);
    typeText("This text appears letter by letter, creating a retro RPG feel.\n\n", 30);
    
    // Demo the progress bar
    cout << "Demonstration of progress bars:" << endl;
    cout << "HP: ";
    drawProgressBar(75, 100, 30);
    
    cout << "MP: ";
    drawProgressBar(50, 100, 30);
    
    cout << "EXP: ";
    drawProgressBar(30, 100, 30);
    
    // Interactive progress bar demo
    cout << "\nLoading your adventure..." << endl;
    for (int i = 0; i <= 100; i += 10) {
        cout << "\r"; // Return to beginning of line
        drawProgressBar(i, 100, 25);
        this_thread::sleep_for(chrono::milliseconds(300));
    }
    
    // Animated battle sequence demo
    cout << "\n\nBattle demonstration:" << endl;
    int playerHP = 100;
    int enemyHP = 80;
    
    typeText("A wild Dragon appeared!\n\n", 40);
    
    // Show initial stats
    cout << "Dragon HP: ";
    drawProgressBar(enemyHP, 80);
    cout << "Your HP: ";
    drawProgressBar(playerHP, 100);
    
    // Simulate a few attack rounds
    typeText("\nYou attack the Dragon!\n", 30);
    this_thread::sleep_for(chrono::milliseconds(500));
    enemyHP -= 20;
    cout << "Dragon HP: ";
    drawProgressBar(enemyHP, 80);
    
    typeText("\nThe Dragon breathes fire at you!\n", 30);
    this_thread::sleep_for(chrono::milliseconds(500));
    playerHP -= 15;
    cout << "Your HP: ";
    drawProgressBar(playerHP, 100);
    
    typeText("\nYou swing your sword with great force!\n", 30);
    this_thread::sleep_for(chrono::milliseconds(500));
    enemyHP -= 30;
    cout << "Dragon HP: ";
    drawProgressBar(enemyHP, 80);
    
    typeText("\nYou defeated the Dragon!\n", 50);
    typeText("You gained 100 EXP!\n", 50);
    
    // Level up animation
    cout << "\nEXP: ";
    for (int i = 70; i <= 100; i += 5) {
        cout << "\r"; // Return to beginning of line
        drawProgressBar(i, 100, 25);
        this_thread::sleep_for(chrono::milliseconds(200));
    }
    
    typeText("\n\nLEVEL UP!\n", 100);
    typeText("Your stats have increased!\n", 50);
    
    typeText("\nThanks for trying this demo!\n", 40);
    
    return 0;
}