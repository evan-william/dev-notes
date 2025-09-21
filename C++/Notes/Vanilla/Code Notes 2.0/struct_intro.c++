#include <iostream>
#include <cmath> // For sqrt function

// Define a struct to represent a 2D point
struct Point {
    // Member variables (fields)
    double x{};
    double y{};

    // Default constructor (called when no values are provided)
    Point() {
        std::cout << "[Default Constructor] Point initialized at (0, 0)\n";
    }

    // Parameterized constructor (called when values are provided)
    Point(double x_val, double y_val) {
        x = x_val;
        y = y_val;
        std::cout << "[Parameterized Constructor] Point initialized at (" << x << ", " << y << ")\n";
    }

    // Member function: print the point
    void print() const {
        std::cout << "Point at (" << x << ", " << y << ")\n";
    }

    // Member function: calculate distance from another point
    double distance_to(const Point& other) const {
        double dx = x - other.x;
        double dy = y - other.y;
        return std::sqrt(dx * dx + dy * dy);
    }

    // Member function: move the point by dx, dy
    void move(double dx, double dy) {
        x += dx;
        y += dy;
    }
};

// Function that takes a struct as parameter
void describe_point(const Point& p) {
    std::cout << "[describe_point] ";
    p.print();
}

// Function that returns a struct
Point make_origin() {
    return Point(0, 0);
}

// Structs can also be nested!
struct Rectangle {
    Point top_left;
    Point bottom_right;

    void print() const {
        std::cout << "Rectangle from ";
        top_left.print();
        std::cout << " to ";
        bottom_right.print();
    }

    double width() const {
        return std::abs(bottom_right.x - top_left.x);
    }

    double height() const {
        return std::abs(top_left.y - bottom_right.y);
    }

    double area() const {
        return width() * height();
    }
};

// Difference between struct and class
class MyClass {
    int secret = 42; // private by default

public:
    void show() {
        std::cout << "MyClass can access secret = " << secret << std::endl;
    }
};

struct MyStruct {
    int open = 42; // public by default

    void show() {
        std::cout << "MyStruct exposes open = " << open << std::endl;
    }
};

int main() {
    std::cout << "=== Basic Point Creation ===\n";
    Point p1; // Calls default constructor
    Point p2(3.0, 4.0); // Calls parameterized constructor

    std::cout << "\n=== Access and Modify Members ===\n";
    p1.x = 1.5;
    p1.y = 2.5;
    p1.print();

    std::cout << "\n=== Using Member Function: distance_to ===\n";
    double dist = p1.distance_to(p2);
    std::cout << "Distance from p1 to p2: " << dist << std::endl;

    std::cout << "\n=== Moving p1 by (+2, +3) ===\n";
    p1.move(2, 3);
    p1.print();

    std::cout << "\n=== Passing Struct to Function ===\n";
    describe_point(p2);

    std::cout << "\n=== Returning Struct from Function ===\n";
    Point origin = make_origin();
    origin.print();

    std::cout << "\n=== Nested Structs: Rectangle ===\n";
    Rectangle rect{Point(1, 5), Point(5, 1)};
    rect.print();
    std::cout << "Width: " << rect.width() << ", Height: " << rect.height() << ", Area: " << rect.area() << std::endl;

    std::cout << "\n=== struct vs class visibility ===\n";
    MyClass c;
    c.show();

    MyStruct s;
    s.show();
    std::cout << "Accessing MyStruct's public variable: " << s.open << std::endl;

    return 0;
}
