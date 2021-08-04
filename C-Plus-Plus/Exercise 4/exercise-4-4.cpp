// Name      : exercise-4-4.cpp
// Purpose   : 
// Modules   : 
// Date      : 4th August 2021 
// Programmer: Gawr Gura

/*
Write a program that asks a user to enter his/her birth month number. The program
then proceeds to display the month in which the user was born as shown below: 

Please Enter Your Birth Month Number: 1
Legends Are Born In January!

Please Enter Your Birth Month Number: 9
Legends Are Born In September!

Ensure that you give appropriate response to a user who enters a month number that
does not exist.

Please Enter Your Birth Month Number: 15
Error. Please enter only values from 1 – 12.

Solve the above problem by using switch…case construct */

#include <iostream>
using namespace std;

int main()
{
    int month;
    cout << "Please Enter Your Birth Month Number : ";
    cin >> month;

    switch (month)
    {
        case 1:
            cout << "Legends Are Born In January!\n";
            break;
        case 2:
            cout << "Legends Are Born In February!\n";
            break;
        case 3:
            cout << "Legends Are Born In March!\n";
            break;
        case 4:
            cout << "Legends Are Born In April!\n";
            break;
        case 5:
            cout << "Legends Are Born In May!\n";
            break;
        case 6:
            cout << "Legends Are Born In June!\n";
            break;
        case 7:
            cout << "Legends Are Born In July!\n";
            break;
        case 8:
            cout << "Legends Are Born In August!\n";
            break;
        case 9:
            cout << "Legends Are Born In September!\n";
            break;
        case 10:
            cout << "Legends Are Born In October!\n";
            break;
        case 11:
            cout << "Legends Are Born In November!\n";
            break;
        case 12:
            cout << "Legends Are Born In December!\n";
            break;
    
        default:
            cout << "Error. Please enter only values from 1 – 12\n";
            break;
    }
}
