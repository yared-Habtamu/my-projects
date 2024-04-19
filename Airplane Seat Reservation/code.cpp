// Airline seat reserevation system
#include <iostream>
#include <cctype>
#include <string>

using namespace std;

int main() {
    //these are variables we use in the below program
    string seatReservation[100][6], fullName, sex, age, passNum, chooseBE, avSeat;
    int tempInt, tempInt2, tempInt3, tempInt4, tempInt5, businesstakenSeats[30] = {}, economytakenSeats[70] = {}, countB = 1, countE = 1;
    bool aleyelem2;
    int k = 0;
    bool error;
    do
    {
    first:
        error = false;
        cout << "\n~~~ WELCOME TO CODECRAFTERS AIRLINES SEAT RESERVATION SYSTEM ~~~" << endl;
        bool tempbool = true; //starting from here the program starts to accept user inputs, here it reads user's full name
        for (int i = 3; i >= 0 && tempbool; --i) //these for loops use to handle invalid input attempts, user will has 4 attempts totally for each inputs
        {
            int error_count = 0;

            cout << "Please Enter Your FULL-NAME:  " << endl;
            getline(cin >> ws, fullName);

            for (char tempChar : fullName)//user name must have to be only alph,and between 5-80
            {
                if (isdigit(tempChar) || fullName.size() > 80 || fullName.size() < 5) {
                    cout << "Invalid Input, Please try Again.(Your Input should only be Alphabets!)\n" << i << " Attempts left." << endl;
                    if (i <= 0)
                    {
                        error = true;
                        goto endcode;
                    }
                    break;
                }
                else {
                    error_count++;
                }
            }
            if(error_count== fullName.size()){
                    tempbool = false;
                }
            }
        
        seatReservation[k][0] = fullName; //here it saves the valid full name to the 2D string

        tempbool = true;
        for (int i = 3; i >= 0 && tempbool; --i)//here it reads user's sex, user's input only must gotta be F/f/M/m
        {
            cout << "Please Enter Your SEX( M for Male, F for female):  " << endl;
            cin >> sex;
            for (char tempChar : sex)
            {
                if (toupper(tempChar) == 'F')
                {
                    sex = "Female";
                    tempbool = false;
                }
                else if (toupper(tempChar) == 'M')
                {
                    sex = "Male";
                    tempbool = false;
                }
                else
                {
                    cout << "Invalid Input, Please try Again.(Your Input should be F or M not-case sesnetive!)\n" << i << " Attempts left." << endl;
                    if (i <= 0)
                    {
                        error = true;
                        goto endcode;
                    }
                    break;
                }
            }
        }
        seatReservation[k][1] = sex;

        tempbool = true;
        for (int i = 3; i >= 0 && tempbool; --i)//here it reads users age , age should be digit and between 0-150[our lines doesnt accept 150+ ppl, for security reason :) ]
        {
            cout << "Please Enter Your AGE:  " << endl;
            cin >> age;
            for (char tempChar : age)
            {
                if (!(isdigit(tempChar)) || stoi(age) > 150 || stoi(age) < 0) {
                    cout << "Invalid Input, Please try Again.(Your Input should be Number!)\n" << i << " Attempts left." << endl;
                    if (i <= 0)
                    {
                        error = true;
                        goto endcode;
                    }
                    break;
                }
                else {
                    tempbool = false;
                }
            }
        }
        seatReservation[k][2] = age;

        tempbool = true;
        for (int i = 3; i >= 0 && tempbool; --i)//based on Ethiopia's Passport Number system, the passport number should have 7 digits and starts with alph
        {
            cout << "Please Enter Your PASSPORT Number:  " << endl;
            cin >> passNum;
            if (!(isalpha(passNum[0])) || passNum.size() != 7) {
                cout << "Invalid Input, Please try Again.(Your Input Should be 7Digits and starsts with alphabet!)\n" << i << " Attempts left." << endl;
                if (i <= 0)
                {
                    error = true;
                    goto endcode;
                }
            }
            else
            {
                for (int j = 0;j<=k ; j++)
                {
                    if (passNum==seatReservation[j][3])
                {
                cout<<"Dear "<<seatReservation[j][0]<<", "<<"You have already reserved a seat. ! "<<endl;
                error=true;
                goto endcode;
                }
    
                }
                break;
            }
        }
        seatReservation[k][3] = passNum;

        tempbool = true;
        for (int i = 3; i >= 0 && tempbool; --i)
        {
            cout << "Please type 1 for First(Business) Class or\nPlease type 2 for Economy Class:  " << endl;
            cin >> chooseBE;

            if (chooseBE == "1") {

                if (countB > 30 && countE <= 70)//checks whether business class seats are full or not
                {
                    cout << "Sorry, All Business Class seats are already reserved. Would you like to reserve in Economy class\n Type 1 for YES, Type Any key for NO" << endl;
                    cin >> tempInt4;
                    if (tempInt4 == 1)
                    {

                        goto mulu;
                    }
                    else
                    {
                        cout << "The next filght will leaves in next 3 hours!" << endl;
                        goto endcode;
                    }
                }
            muluE:
                seatReservation[k][4] = "BusinessClass";
                countB++;
                break;
            }
            else if (chooseBE == "2") {
                if (countE > 70 && countB <= 30)//checks whether economy class seats are full or not
                {
                    cout << "Sorry, All Economy Class seats are already reserved. Would you like to reserve in Business class\n Type 1 for YES, Type Any key for NO" << endl;
                    cin >> tempInt4;
                    if (tempInt4 == 1)
                    {

                        goto muluE;
                    }
                    else
                    {
                        cout << "The next filght will leaves in next 3 hours!" << endl;
                        goto endcode;
                    }
                }
            mulu:
                seatReservation[k][4] = "EconomyClass";
                countE++;
                break;
            }
            else {
                cout << "Invalid Input, Please try Again.(Your Input should only be 1 or 2 !)\n" << i << " Attempts left." << endl;
                if (i <= 0)
                {
                    error = true;
                    goto endcode;
                }
            }
        }

        cout << "Would You Like To See The Avalaible Seats Before Choosing Seat Number(Type 1 for YES, ANy key for NO):   " << endl;
        cin >> avSeat;
        if (avSeat == "1") {//here the program prints seats with info of reserved or not
            if (seatReservation[k][4] == "BusinessClass")
            {
                for (int i = 1; i <= 30; i++)
                {
                    bool aleyelem = false;
                    for (int value : businesstakenSeats)
                    {
                        if (value == i)
                        {
                            aleyelem = true;
                            break;
                        }
                    }
                    (aleyelem ? cout << "[#" << i << "X\t:( RESE]  " : cout << "[#" << i << "\t:) FREE]  ");

                    if (i % 2 == 0)
                    {
                        cout << endl;
                    }
                }

            }
            else
            {
                for (int i = 31; i <= 100; i++)
                {
                    bool aleyelem = false;
                    for (int value : economytakenSeats)
                    {
                        if (value == i)
                        {
                            aleyelem = true;
                            break;
                        }
                    }

                    (aleyelem ? cout << "[#" << i << "X\t:( RESE]  " : cout << "[#" << i << "\t:) FREE]  ");
                    if (i % 5 == 0)
                    {
                        cout << endl;
                    }
                }
            }

        }
    chooseSeat:

        if (seatReservation[k][4] == "BusinessClass")//let the user choose available seats 
        {
            tempbool = true;
            for (int i = 3; i >= 0 && tempbool; --i)
            {
                cout << "\nNow, Please Choose Seat Number(01-30):  " << endl;
                cin >> tempInt3;
                if (tempInt3 < 1 || tempInt3>30)
                {
                    cout << "Invalid Input, Please try Again.(Your Input should only be from 1-30 !)\n" << i << " Attempts left." << endl;
                    if (i <= 0)
                    {
                        error = true;
                        goto endcode;
                    }
                }
                else
                {
                    break;
                }

            }
            aleyelem2 = false;
            for (int value : businesstakenSeats)
            {
                if (value == tempInt3)
                {
                    aleyelem2 = true;
                    break;
                }

            }
            businesstakenSeats[k] = tempInt3;
            if (aleyelem2)
            {
                cout << "Seat Number " << tempInt3 << " is not AVAILABLE! Please TRY AGAIN." << endl;
                goto chooseSeat;
            }
        }
        else
        {
            tempbool = true;
            for (int i = 3; i >= 0 && tempbool; --i)
            {
                cout << "Now, Please Choose Seat Number(31-100):  " << endl;
                cin >> tempInt3;
                if (tempInt3 < 31 || tempInt3>100)
                {
                    cout << "Invalid Input, Please try Again.(Your Input should only be from 31-100!)\n" << i << " Attempts left." << endl;
                    if (i <= 0)
                    {
                        error = true;
                        goto endcode;
                    }
                }
                else
                {
                    break;
                }
            }
            aleyelem2 = false;
            for (int value : economytakenSeats)
            {
                if (value == tempInt3)
                {
                    aleyelem2 = true;
                    break;
                }

            }
            economytakenSeats[k] = tempInt3;
            if (aleyelem2)
            {
                cout << "Seat Number " << tempInt3 << " is not AVAILABLE! Please TRY AGAIN." << endl;
                goto chooseSeat;
            }
        }

        seatReservation[k][5] = to_string(tempInt3);
        string boardinPass;//the boarding pass of the customers is going to be a string concatinated from the first letter of their name + first 3 characters of their passport number+ B or E based on their class+their seat number
        char letter = toupper(seatReservation[k][3][0]);
        boardinPass += toupper(seatReservation[k][0][0]);
        boardinPass = boardinPass + letter + seatReservation[k][3][1] + seatReservation[k][3][2] + seatReservation[k][4][0] + seatReservation[k][5];

        seatReservation[k][6] = boardinPass;
        cout << "~~~ Congrats, You have successfully resereved a Seat. ~~~\n \t Seat Number - " << seatReservation[k][5] << "\n \t Class -- " << seatReservation[k][4] << "\n \t Boarding Pass - " << seatReservation[k][6] << endl;
        cout << "\n\t~~~~~~~ SAFE FLIGHT ~~~~~~~" << endl;


        k++;
    } while (k < 100);

endcode:
    if (error)
    {
        cout << "Sorry, Your previous informations have been CANCELED.Please try again later.\n\t Thank You for choosing us !" << endl;
        k--;
        goto first;
    }
    cout << "Prgoram Finished! " << endl;
    return 0;
}
