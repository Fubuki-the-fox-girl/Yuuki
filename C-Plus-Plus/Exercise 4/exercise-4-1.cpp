// Name      : exercise-4-1.cpp
// Purpose   : 
// Modules   : 
// Date      : 4th August 2021 
// Programmer: Gawr Gura


// Write a complete program that asks a user to enter a number. If the number is 
// Positive, the program will display “Positive Number” and if the number is Negative, 
// the program will display “Negative Number”. If the user enters 0 (zero), the program 
// will display “Neutral Number”. Please use if constructs to solve this problem.

#include <iostream>
using namespace std;

int main()
{
    int int1;

    cout << "Please simply enter an integers ...\n";
    cin >> int1;
    if (int1 > 0)
    {
        cout << "It is a positive number !!!";
    }
    else if (int1 < 0)
    {
        cout << "It is a negative number ...";
    }
    else
    {
        cout << "It's neutral !?!";
    }
    return 0;
}


