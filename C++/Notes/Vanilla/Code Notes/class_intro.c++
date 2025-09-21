#include <iostream>
using namespace std;

const double PI {3.142857142857143};
class Cylinder { // MEMBERS IS PRIVATE BY DEFAULT
    public : // Public means the memory in this class can be accessible outside of the class. ( LIKE USED IN MAIN)
    /*
        CAN ACTUALLY MAKE PUBLIC OF THE volume() and no need to make public of the base_radius and height and it will
        automatically make everything inside the volume() public INCLUDING the base_radius and height
    */
        double base_radius {1.0};
        double height {1.0};
    public :    
        double volume(){
            return PI * base_radius * base_radius * height;
        }
};

/* NOW WHEN ITS MADE PRIVATE, EVERYTHING INSIDE THE PRIVATE CANT BE ACCESSED OUTSIDE, SO LIKE COUT << height IS NOT POSSIBLE!
class Cylinder { 
    private :    
        double base_radius {1.0};
        double height {1.0};
    public :    
        double volume(){
            return PI * base_radius * base_radius * height;
        }
};
*/

int main () {
    Cylinder cylinder1; 
    cout << "volume c1 : " << cylinder1.volume() << endl; // ACCESIBLE CUZ PUBLIC!!

    cylinder1.base_radius = 3.0;
    cylinder1.height = 2;   
    cout << "volume c1: " << cylinder1.volume() << endl;

    Cylinder cylinder2;
    cout << "volume c2: " << cylinder2.volume() << endl;

    return 0;
}