#include <iostream>

int main() {
    // --------------------------------------------------------------------
    // 1. Lambda function with no parameters and no return type
    // --------------------------------------------------------------------
    auto func = []() {
        std::cout << "[1] Hello World!" << std::endl;
    };

    func(); // Call the lambda
    func(); // Call it again

    // --------------------------------------------------------------------
    // 2. Lambda function called immediately (anonymous and direct call)
    // --------------------------------------------------------------------
    []() {
        std::cout << "[2] This is a direct call of a lambda" << std::endl;
    }(); // <- note the parentheses at the end to call it

    // --------------------------------------------------------------------
    // 3. Lambda function that takes parameters and prints result
    // --------------------------------------------------------------------
    [](double a, double b) {
        std::cout << "[3] a + b : " << (a + b) << std::endl;
    }(10.0, 50.0); // Passing arguments directly

    // --------------------------------------------------------------------
    // 4. Storing lambda with parameters and reusing it
    // --------------------------------------------------------------------
    auto func1 = [](double a, double b) {
        std::cout << "[4] a + b : " << (a + b) << std::endl;
    };

    func1(10, 20);
    func1(5, 7);

    // --------------------------------------------------------------------
    // 5. Lambda that returns a value (called immediately)
    // --------------------------------------------------------------------
    auto result = [](double a, double b) {
        return a + b;
    }(10, 60); // Result is 70

    std::cout << "[5] result : " << result << std::endl;

    // --------------------------------------------------------------------
    // 6. Storing a return-value lambda in a variable and using it multiple times
    // --------------------------------------------------------------------
    auto func2 = [](double a, double b) {
        return a + b;
    };

    auto result1 = func2(23, 7);  // 30
    auto result2 = func2(9, 45);  // 54

    std::cout << "[6] result1 : " << result1 << std::endl;
    std::cout << "[6] result2 : " << result2 << std::endl;
    std::cout << "[6] direct call : " << func2(5, 2) << std::endl;

    // --------------------------------------------------------------------
    // 7. Lambda with explicit return type (int), even if inputs are double
    // --------------------------------------------------------------------
    auto func3 = [](double a, double b) -> int {
        return a + b;  // Result will be casted to int (fraction dropped)
    };

    // Same lambda but with implicit return type (will be double here)
    auto func4 = [](double a, double b) {
        return a + b;
    };

    double a{6.9};
    double b{3.5};

    auto result3 = func3(a, b); // Returns int -> 10
    auto result4 = func4(a, b); // Returns double -> 10.4

    std::cout << "[7] result3 (int) : " << result3 << std::endl;
    std::cout << "[7] result4 (double) : " << result4 << std::endl;

    std::cout << "[7] sizeof(result3) (int) : " << sizeof(result3) << std::endl; // Typically 4 bytes
    std::cout << "[7] sizeof(result4) (double) : " << sizeof(result4) << std::endl; // Typically 8 bytes

    // --------------------------------------------------------------------
    // 8. Capture lists: capture values from outer scope into lambda
    // --------------------------------------------------------------------
    {
        std::cout << "\n[8] Capture List (by value)" << std::endl;
        double x{10};
        double y{20};

        auto captureByValue = [x, y]() {
            std::cout << "x + y : " << x + y << std::endl;
        };

        captureByValue(); // Outputs 30
    }

    // --------------------------------------------------------------------
    // 9. Capture by VALUE demo - value copied, outer value doesn't change
    // --------------------------------------------------------------------
    {
        std::cout << "\n[9] Capture by VALUE" << std::endl;

        int c{42};

        auto func = [c]() {
            std::cout << "Inner value : " << c << " | &inner : " << &c << std::endl;
        };

        for (size_t i{}; i < 5; ++i) {
            std::cout << "Outer value : " << c << " | &outer : " << &c << std::endl;
            func(); // Inner value stays the same because it's a COPY
            ++c;    // Only outer value changes
        }
    }

    // --------------------------------------------------------------------
    // 10. Capture by REFERENCE demo - changes reflected inside lambda
    // --------------------------------------------------------------------
    {
        std::cout << "\n[10] Capture by REFERENCE" << std::endl;

        int c{42};

        auto func = [&c]() {
            std::cout << "Inner value : " << c << " | &inner : " << &c << std::endl;
        };

        for (size_t i{}; i < 5; ++i) {
            std::cout << "Outer value : " << c << " | &outer : " << &c << std::endl;
            func(); // Inner value also changes because it's a reference
            ++c;
        }
    }

     // --------------------------------------------------------------------
    // 11. Capture ALL by VALUE using [=]
    // --------------------------------------------------------------------
    {
        std::cout << "\n[11] Capture all by VALUE [=]" << std::endl;

        int a{100};
        int b{200};

        auto func = [=]() {
            std::cout << "Inside lambda - a : " << a << ", b : " << b << std::endl;
        };

        for (int i = 0; i < 3; ++i) {
            std::cout << "Outer loop - a : " << a << ", b : " << b << std::endl;
            func(); // Uses original copies
            ++a;
            ++b;
        }

        /*
            Explanation:
            - [=] captures ALL variables used inside the lambda by VALUE (copy).
            - So even when outer a and b are modified, lambda uses their original values.
        */
    }

    // --------------------------------------------------------------------
    // 12. Capture ALL by REFERENCE using [&]
    // --------------------------------------------------------------------
    {
        std::cout << "\n[12] Capture all by REFERENCE [&]" << std::endl;

        int a{100};
        int b{200};

        auto func = [&]() {
            std::cout << "Inside lambda - a : " << a << ", b : " << b << std::endl;
        };

        for (int i = 0; i < 3; ++i) {
            std::cout << "Outer loop - a : " << a << ", b : " << b << std::endl;
            func(); // Reflects updated values
            ++a;
            ++b;
        }

        /*
            Explanation:
            - [&] captures ALL variables used inside the lambda by REFERENCE.
            - Lambda sees updated values of a and b on every call.
        */
    }

    std::cout << "\nDone!" << std::endl;
    return 0;
}
