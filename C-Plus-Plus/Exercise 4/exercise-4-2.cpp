// Name      : exercise-4-2.cpp
// Purpose   : 
// Modules   : 
// Date      : 4th August 2021 
// Programmer: Gawr Gura


// Requests for the user’s age and determine if he/she can watch a movie rated as P18 (i.e. only viewer 18 or above are allowed to watch) using:
// a) conditional operator
// b) if constructs
// c) if…else construct

#include <iostream>
using namespace std;


int main()
{
    int age;
    cout << "How old are you ?\n";
    cin >> age;

    if (age >= 18) {
        cout << "Wow u r a big boy / girl now !!!";
    }
    else {
        cout << "Smollllllllll";
    }
    return 0;
}