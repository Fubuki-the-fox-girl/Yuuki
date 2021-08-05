// Name      : lab-4-3.cpp
// Purpose   : 
// Modules   : 
// Date      : 5th August 2021 
// Programmer: Gawr Gura

/*
Write a program that asks a user to enter 3 numbers. Following that the program
displays the highest number entered. The output of the program is given below:

Please Enter Three Numbers:
78
44
85
The Highest Number Entered is: 85

Use multiple if constructs or nested if…else construct to complete this program by
testing your program with the following combinations of numbers:

Num1    Num2    Num3    Highest value shown
3       2       1       3
1       3       2       3
1       2       3       3
3       3       3       3 (from any variable)
3       1       3       3 (from Num1 or Num3)
3       3       1       3 (from Num1 or Num2)
1       3       3       3 (from Num2 or Num3) */

#include <iostream>
using namespace std;

int main() {
    int int1, int2, int3;
    cout << "Please Enter Three Numbers:\n";
    cin >> int1 >> int2 >> int3;

    if (int1 >= int2 and int1 >= int3) {
        cout << "The Highest Number Entered is: " << int1;
    } else if (int2 >= int1 and int2 >= int3) {
        cout << "The Highest Number Entered is: " << int2;
    } else if (int3 >= int1 and int3 >= int2) {
        cout << "The Highest Number Entered is: " << int3;
    }
}