// Name      : exercise-4-3.cpp
// Purpose   : 
// Modules   : 
// Date      : 4th August 2021 
// Programmer: Gawr Gura

/*
Write a program that requests for a user to enter his/her height (in m) and weight (in
kg). The program then calculates the Body Mass Index (BMI) for the user.
a) If the BMI is >=19 and <=25, the program will display “Your BMI is within
the normal range”.
b) If the calculated BMI value is >25, the program will display “You are
overweight”.
c) If the BMI value is <19, the program will display “You are underweight”.
Please use if constructs to solve this problem. Below is the sample output of the
program.

Please enter your height (in m): 1.75
Please enter your weight (in kg): 75
Your BMI is within the normal range.

(Hint: BMI = weight/height2) */

#include <iostream>
using namespace std;

int main()
{
    float weight;
    float height;
    float bmi;

    cout << "How heavy are you ?\n";
    cin >> weight;
    cout << "How tall are you?\n";
    cin >> height;

    bmi = (weight)/(height*height);
    
    cout << bmi << endl;
    if (weight < 0 or height < 0) {
        cout << "Invalid value";
    }
    else if (19 <= bmi <= 25) {
        cout << "Your BMI is within the normal range , haha";
    }
    else if (bmi > 25) {
        cout << "You are overweight babi" ;
    }
    else if (bmi < 19) {
        cout << "You are underweight";
    }
    return 0;
}