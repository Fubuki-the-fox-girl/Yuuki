// Name      : exercise-4-5.cpp
// Purpose   : 
// Modules   : 
// Date      : 4th August 2021 
// Programmer: Gawr Gura

/*
Write a program that prompts a user to enter two numbers. Once entered, the
program will request for the user to choose a mathematical operation (i.e. Calculate
Sum or Difference). Then the program displays the answer to the operation carried
out to the two numbers based on the selection of mathematical operator. Sample
outputs of the program are given below:

Please enter two numbers:
5
8
Please Select An Arithmetic Operation Below:
1) Sum
2) Difference
Option: 1
The Sum of 5 and 8 is 13.

Please enter two numbers:
5
8
Please Select An Arithmetic Operation Below:
1) Sum
2) Difference
Option: 2
The Difference of 5 and 8 is 3.

Please use switch…case and if constructs to solve this problem. (Reminder: For
calculating the difference, make sure the displayed value is kept as a positive
number). */

#include <iostream>
using namespace std;

int main() {
    float int1, int2, sum, diff;
    int option;
    cout << "Please enter two numbers:\n";
    cin >> int1 >> int2;

    cout << "Please Select An Arithmetic Operation Below:\n1) Sum\n2) Difference\nOption: ";
    cin >> option;

    switch (option)
    {
    case 1:
        sum = int1 + int2;
        cout << "\nThe Sum of " << int1 << " and " << int2 << " is " << sum;
        break;
    case 2:
        if (int1 >= int2) {
            diff = int1 - int2;
            cout << "\nThe Difference of " << int1 << " and " << int2 << " is " << diff;
        } else {
            diff = int2 - int1;
            cout << "\nThe Difference of " << int2 << " and " << int1 << " is " << diff;
        }
        break;

    default:
        cout << "Invalid options ...";
        break;
    }

    return 0;
}
