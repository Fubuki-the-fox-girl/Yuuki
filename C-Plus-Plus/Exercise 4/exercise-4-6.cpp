// Name      : exercise-4-6.cpp
// Purpose   : 
// Modules   : 
// Date      : 4th August 2021 
// Programmer: Gawr Gura

/*
Create a program to calculate the average of temperature readings. First, the
program will request from the user to select either two or three temperature readings
to be entered. Following that, the program then requests to enter the temperature
readings (i.e. 2 or 3 readings based on the option chosen earlier), calculates the
average reading and display the average reading. Please use switch case construct
to complete this program.

Please select number of readings:
1- For calculating 2 temperature readings
2- For calculating 3 temperature readings
Selection: 1
Please Enter 2 readings:
45.5
46.7
The average readings for 2 values entered is: 46.1

Please select number of readings:
1- For calculating 2 temperature readings
2- For calculating 3 temperature readings
Selection: 2
Please Enter 3 readings:
45.5
46.7
44.3
The average readings for 3 values entered is: 45.4

Please select number of readings:
1- For calculating 2 temperature readings
2- For calculating 3 temperature readings
Selection: 5
Invalid Selection! Please restart the program. */

#include <iostream>
using namespace std;

int main() {
    int option;
    float temp1, temp2, temp3, average;

    cout << "Please select number of readings:\n1- For calculating 2 temperature readings\n2- For calculating 3 temperature readings\nSelection: ";
    cin >> option;

    switch (option)
    {
        case 1:
        cout << "Please Enter 2 readings:\n";
        cin >> temp1 >> temp2;

        average = (temp1 + temp2) / 2;
        cout << "The average readings for 2 values entered is: " << average;
        break;

        case 2:
        cout << "Please Enter 3 readings:\n";
        cin >> temp1 >> temp2 >> temp3;

        average = (temp1 + temp2 + temp3) / 3;
        cout << "The average readings for 3 values entered is: " << average;
        break;

        default:
        cout << "Invalid Selection! Please restart the program.";
        break;
    }

    return 0;
}
