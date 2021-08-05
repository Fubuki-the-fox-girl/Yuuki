// Name      : lab-4-2.cpp
// Purpose   : 
// Modules   : 
// Date      : 5th August 2021 
// Programmer: Gawr Gura

/*
Write a program that asks an objective question and depending on the answer
displays “You are Right!” or “You are Wrong!” A sample output of the program is given
below

The Operator ‘=’ is known as:
(A) Comparison Operator
(B) Assignment Operator
(C) Logical Operator
(D) Unary Operator
Answer: B
You are Right!

Use the switch…case construct to solve the above problem. Ensure that the program
can accept and respond to lowercase characters as the answer. */

#include <iostream>
using namespace std;

int main() {
    char ans;
    cout << "The Operator ‘=’ is known as:\n(A) Comparison Operator\n(B) Assignment Operator\n(C) Logical Operator\n(D) Unary Operator\nAnswer: ";
    cin >> ans;

    switch (ans) {
        case 'B' :
        case 'b' :{
            cout << "You are Right!";
            break;
        }

        case 'A' :
        case 'a' :
        case 'C' :
        case 'c' :
        case 'D' :
        case 'd' : {
            cout << "You are Wrong!";
            break;
        }

        default: {
            cout << "Invalid option!";
        }

    }
}