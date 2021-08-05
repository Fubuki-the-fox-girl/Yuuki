// Name      : lab-4-1.cpp
// Purpose   : 
// Modules   : 
// Date      : 5th August 2021 
// Programmer: Gawr Gura

/*
Write a program that asks a user to enter his/her age. If the age is >=15 and <=25,
the program displays “Wanna Be Friends?” and if any other age is entered, the
program displays “Sorry! You are not suitable to be my friend!” A sample output of
the program is given below: 

Please Enter Your Age: 14
Sorry! You are not suitable to be my friend!

Solve this problem by using if construct OR if…else construct. */

#include <iostream>
using namespace std;

int main() {
    int age;

    cout << "Please Enter Your Age:\n";
    cin >> age;

    if (15 <= age and age <= 25) {
        cout << "Wanna Be Friends?";
    } else {
        cout << "Sorry! You are not suitable to be my friend!";
    }

    return 0;
}