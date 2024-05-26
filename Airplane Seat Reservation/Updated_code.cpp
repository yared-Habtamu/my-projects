#include <iostream>
#include <vector>
#include <cctype>
#include <string>
#include <fstream>
#include <iomanip>
using namespace std;

class SeatReservationSystem {
private:
    struct Reservation {
        string fullName;
        string sex;
        string age;
        string passNum;
        string classType;
        string seatNumber;
        string boardingPass;
    };

    vector<Reservation> seatReservation;
    int countB;
    int countE;
    int businesstakenSeats[30] = {};
    int economytakenSeats[70] = {};

    bool isValidFullName(const string& fullName) {
        for (char tempChar : fullName) {
            if (tempChar == ' ' || isalpha(tempChar)) {
                continue;
            }
            else {
                return false;
            }
        }
        return fullName.size() >= 2 && fullName.size() <= 80;
    }

    bool isValidPassportNum(const string& passNum) {
        return isalpha(passNum[0]) && passNum.size() == 7;
    }

    bool isValidAge(const string& age) {
        for (char tempChar : age) {
            if (!isdigit(tempChar)) {
                return false;
            }
        }
        int ageNum = stoi(age);
        return ageNum >= 0 && ageNum <= 150;
    }

    bool isValidSex(const string& sex) {
        if (sex[0] == 'M' || sex[0] == 'F' || sex[0] == 'm' || sex[0] == 'f') {
            return true;
        }
        else {
            return false;
        }
    }
    bool isSeatAvailable(const string& classType, int seatNumber) {
        ifstream inFile("reservations.txt");
        string line;

        if (!inFile) {
            cerr << "Unable to open file" << endl;
            return false;
        }

        while (getline(inFile, line)) {
            if (line.find("Seat Number: " + to_string(seatNumber)) != string::npos) {
                inFile.close();
                return false;
            }
        }

        inFile.close();
        return true;
    }

public:
    SeatReservationSystem() : countB(1), countE(1) {}
    void displayDestinations() {
        cout << "\nToday's Destinations from Addis Ababa, Ethiopia : to\n\n";
        cout << "\t\t1. Nairobi, Kenya  \t\t 11. Germany: Berlin\n";
        cout << "\t\t2. Cairo, Egypt    \t\t 12. Spain: Madridn\n";
        cout << "\t\t3. USA Washington  \t\t 13. Serbia: Belgraden\n";
        cout << "\t\t4. Lagos, Nigeria  \t\t 14. Argentina: BounesAires\n";
        cout << "\t\t5. Accra, Ghana    \t\t 15. Norway: Oslo\n";
        cout << "\t\t6. Dakar, Senegal  \t\t 16. Russia: Moscow\n";
        cout << "\t\t7. Mekele,Ethiopia \t\t 17. Ukraine: Kyiv\n";
        cout << "\t\t8. Tunis, Tunisia  \t\t 18. United Kingdom: London\n";
        cout << "\t\t9. Jimma,Ethiopia    \t\t19. Brazil.Brasillia\n";
        cout << "\t\t10. Luanda, Angol    \t\t20. Johansberg, South Africa\n";


    }
    void displayfromfile(char adminchoice,const string& password) {
        if (password == "codecrafters123") {
            if (adminchoice == '1') {
            ifstream file("reservations.txt");
            if (file.is_open()) {
                string line;
                cout << left << setw(20) << "Full Name" << setw(20) << "Passport Number" << setw(20) << "Boarding Pass" << endl;
                cout << "---------------------------------------------------------------------" << endl;
                while (getline(file, line)) {
                    if (line.find("Full Name:") != string::npos) {
                        cout << setw(20) << line.substr(line.find(":") + 2);
                    } else if (line.find("Passport Number:") != string::npos) {
                        cout << setw(20) << line.substr(line.find(":") + 2);
                    } else if (line.find("Boarding Pass:") != string::npos) {
                        cout << setw(20) << line.substr(line.find(":") + 2) << endl;
                    }
                }
                file.close();
            } else {
                cout << "Unable to open file" << endl;
            }
        }
        }
         else {
            cout << "Incorrect password. You can't see details" << endl;
        }
        
    }


    void clearFile(const string& password) {
        if (password == "codecrafters123") {
            ofstream file("reservations.txt", ofstream::trunc);
            cout << "All information in the file has been cleared." << endl;
            file.close();
        }
        else {
            cout << "Incorrect password. File not cleared." << endl;
        }
    }

    void displayAvailableSeats(const string& classType) {
        cout << "Available Seats for " << classType << " Class:" << endl;
        ifstream inFile("reservations.txt");
        string line;

        if (!inFile) {
            cerr << "Unable to open file" << endl;
            return;
        }

        int seatCounter = 0;
        if (classType == "BusinessClass") {
            for (int i = 1; i <= 30; i++) {
                bool isReserved = false;
                inFile.clear();
                inFile.seekg(0, ios::beg);
                while (getline(inFile, line)) {
                    if (line.find("Seat Number: " + to_string(i)) != string::npos) {
                        isReserved = true;
                        break;
                    }
                }
                string status = isReserved ? "\t:(  RESERVED ]" : "\t:) IT'S FREE ]" ;
                cout << "\t\t[  " << setw(2) << i << " " << status << "  ";
                if (++seatCounter % 4 == 0) {
                    cout << "\n";
                }
            }
        }
        else {
            for (int i = 31; i <= 100; ++i) {
                bool isReserved = false;
                inFile.clear();
                inFile.seekg(0, ios::beg);
                while (getline(inFile, line)) {
                    if (line.find("Seat Number: " + to_string(i)) != string::npos) {
                        isReserved = true;
                        break;
                    }
                }
                string status = isReserved ? "\t:(  RESERVED ]" : "\t:) IT'S FREE ]" ;
                cout << "\t\t[  " << setw(2) << i << " " << status << "  ";
                if (++seatCounter % 4 == 0) {
                    cout << endl;
                }
            }
        }

        inFile.close();
    }


    void makeReservation() {
        Reservation newReservation;
    again:
        cout << "\nPlease Enter Your FULL-NAME: ";
        for (int i = 3; i >= 0; i--)
        {
            getline(cin >> ws, newReservation.fullName);
            if (!isValidFullName(newReservation.fullName)) {
                cout << "Error!! \n you have " << i << " chance left ";
                cout << "\n Name should be only English letter ";
                if (i == 0) {
                    cout << "  Sorry you can't continue,Try again!!" << endl;
                    goto again;
                }
                else {
                    cout << "Error!!\nEnter your Full name again : ";
                }
            }
            else {
                break;
            }

        }
        cout << "\nPlease Enter Your SEX: ";
        for (int i = 3; i >= 0; i--) {
            cin >> newReservation.sex;
            if (!isValidSex(newReservation.sex)) {
                cout << "Error!! \n you have " << i << " chance left ";
                cout << "\n Sex should be Male or Female ";
                if (i == 0) {
                    cout << "  Sorry you can't continue,Try again!!" << endl;
                    goto again;
                }
                else {
                    cout << "\n Enter your Sex correctly : ";
                }
            }
            else {
                newReservation.sex = (toupper(newReservation.sex[0]) == 'F') ? "Female" : "Male";
                break;
            }
        }
        cout << "\nPlease Enter Your AGE: ";
        for (int i = 3; i >= 0; i--) {
            cin >> newReservation.age;
            if (!isValidAge(newReservation.age)) {
                cout << "Error!! \n you have " << i << " chance left ";
                cout << "\n Age should between 1 and 150";
                if (i == 0) {
                    cout << "  Sorry you can't continue,Try again!!" << endl;
                    goto again;
                }
                else {
                    cout << "\nEnter your Age again : ";
                }
            }
            else {
                break;
            }
        }

        cout << "\nPlease Enter Your PASSPORT Number: ";
        for (int i = 3; i >= 0; i--) {
            cin >> newReservation.passNum;
            if (!isValidPassportNum(newReservation.passNum)) {
                cout << "Error!! \n you have " << i << " chance left ";
                cout << "\n Passport number should be start with Letter and have 7 character";
                if (i == 0) {
                    cout << "  Sorry you can't continue,Try again!!" << endl;
                    goto again;
                }
                else {
                    cout << "\nEnter your Passport number again  correctly: ";
                }
            }
            else {
                break;
            }
        }


        void checkExistingReservation(const Reservation & newReservation); {
            ifstream file("reservations.txt");
            Reservation res;

            if (file.is_open()) {
                while (file >> res.passNum >> res.fullName) {
                    if (newReservation.passNum == res.passNum) {
                        cout << "Dear " << res.fullName << ", You have already reserved a seat!" << endl;
                        file.close();
                        return;
                    }
                }
                file.close();
            }
            else {
                cerr << "Unable to open file!" << endl;
            }
        }

        cout << "\n1: Business Class";
        cout<< "\n2: Economy Class: ";
        cout<<"\nEnter Your Class Type: ";
        cin >> newReservation.classType;
        newReservation.classType = (newReservation.classType == "1") ? "BusinessClass" : "EconomyClass";

        displayAvailableSeats(newReservation.classType);

        cout << "\n\nPlease Choose Unreserved Seat Number: ";
        do {
            cin >> newReservation.seatNumber;
            if (newReservation.classType == "BusinessClass") {
                if (stoi(newReservation.seatNumber) < 1 || stoi(newReservation.seatNumber) > 30 ||
                    !isSeatAvailable("BusinessClass", stoi(newReservation.seatNumber))) {
                    cout << "Invalid Seat. Please choose another: ";
                }
                else {
                    businesstakenSeats[countB++] = stoi(newReservation.seatNumber);
                    break;
                }
            }
            else {
                if (stoi(newReservation.seatNumber) < 31 || stoi(newReservation.seatNumber) > 100 ||
                    !isSeatAvailable("EconomyClass", stoi(newReservation.seatNumber))) {
                    cout << "Invalid Seat. Please choose another: ";
                }
                else {
                    economytakenSeats[countE++] = stoi(newReservation.seatNumber);
                    break;
                }
            }
        } while (true);

        char letter = toupper(newReservation.passNum[0]);
        newReservation.boardingPass = string(1, toupper(newReservation.fullName[0])) +
            string(1, letter) +
            newReservation.passNum.substr(1, 2) +
            newReservation.classType[0] +
            newReservation.seatNumber;

        seatReservation.push_back(newReservation);

        cout << "\n\t\t\t\t~ ~ ~  Congrats," << newReservation.fullName << " You have successfully reserved a Seat. ~ ~ ~" << endl;
        cout << "\t\t\tYour seat number is " << newReservation.seatNumber << endl;
        cout << "\t\t\tClass: " << newReservation.classType << endl;
        cout << "\t\t\tBoarding Pass: " << newReservation.boardingPass << endl;
        cout << "\n\n\t\t\t\t\t~ ~ ~ ~ ~ ~  SAFE FLIGHT ~ ~ ~ ~ ~ ~ ~ " << endl;
        ofstream reservationFile("reservations.txt", ios::app);
        if (reservationFile.is_open()) {
            reservationFile << "Full Name: " << newReservation.fullName << endl;
            reservationFile << "Sex: " << newReservation.sex << endl;
            reservationFile << "Age: " << newReservation.age << endl;
            reservationFile << "Passport Number: " << newReservation.passNum << endl;
            reservationFile << "Class Type: " << newReservation.classType << endl;
            reservationFile << "Seat Number: " << newReservation.seatNumber << endl;
            reservationFile << "Boarding Pass: " << newReservation.boardingPass << endl;
            reservationFile << "\n++++++++++++++++++++++++++"<<endl;
            reservationFile.close();
        }
        else {
            cout << "Unable to open file for reservation storage." << endl;
        }
        seatReservation.push_back(newReservation);
        cout << "Reservation details saved successfully." << endl;
    }


};
int main() {
    cout << "\n \t\t\t\t\t\t * * *  W E L C O M E   T O   C O D E C R A F T E R S   A I R L I N E S   * * * " << endl;

    SeatReservationSystem reservationSystem;
    char choose;
    bool close = false;
    do {
        cout << "\n\n \t\t\t\t Menu\n";
        cout << "\n\t\t1, Registration \n";
        cout << "\t\t2, See Available Seats \n";
        cout << "\t\t3, See Todays Destinations\n";
        cout << "\t\t4, Run as an Administrator \n";
        cout << "\t\t5, Quit The Program\n";

        cout << "\nPlease, Choose! : ";
        cin >> choose;
        if (choose == '1')
        {
            reservationSystem.makeReservation();
            int n;
            cout << "Press 1 to clear the terminal: ";
            cin >> n;
            system("cls");

        }
        else if (choose == '2')
        {
            char x;
            cout << "1, Economy Class\n";
            cout << "2, Business Class\n";
            cout << "Enter your choice ";
            for(int i=0;i<3;i++){
                cin >> x;
                if (x == '1') {
                    reservationSystem.displayAvailableSeats("EconomyClass");
                    break;
                }
                else if (x == '2') {
                    reservationSystem.displayAvailableSeats("BusinessClass");
                    break;
                }
                else{
                    if(i==2){
                        cout<<"\nTry again";
                        break;
                    }
                    cout<<"Please, Enter correspondigly you have left with "<<3-(i+1)<<" chances : ";
                }

            }

        }
        else if (choose == '3') {
            reservationSystem.displayDestinations();
        }
        else if (choose == '4') {
            cout << "Enter Password to Run as Administrator: ";
            string pass;
            char adminchoice;
            cin >> pass;
            cout<<"1, See Data Base Details \n";
            cout<<"2, Clear all Data Files \n";
            cin>>adminchoice;
            for(int chance=0;chance<3;chance++){
                if(adminchoice=='1'){
                    reservationSystem.displayfromfile(adminchoice,pass);
                    break;
                }
                else if(adminchoice=='2'){
                    reservationSystem.clearFile(pass);
                    break;
                }        
                else{
                    cout<<"\nYou have Entered Invalid input press 1 or 2  only";
                    cout<<3-(chance+1)<<" chance left";
                    if(chance==2){
                        break;
                    }
                }

            }    
            
        }
    } while (choose!='5');

    cout << "\nProgram Finished!" << endl;
    return 0;
}
