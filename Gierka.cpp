/*Wszystkie pliki biblioteki itp.*/
#include <iostream>
#include <windows.h>
/*pliki pierwszej komnaty*/
#include "sceletonF.cpp"
#include "sceletonR.cpp"
#include "boatB.cpp"
#include "sceletonE.cpp"
#include "drowning.cpp"
#include "boatR.cpp"
#include "ratE.cpp"
#include "ratT.cpp"
#include "ratP.cpp"
/*pliki drugiej komnaty*/
#include "womanE.cpp"
#include "vampireM.cpp"
#include "bartenderE.cpp"
#include "bartenderP.cpp"
#include "bartenderD.cpp"
#include "priestE.cpp"
#include "priestF.cpp"
/*koniec*/
#include "treasure.cpp"
using namespace std;
/*Dane gracza*/
class player {
public:
  string traveler = "";
  string weapon = "";
};
int choice;
int random;
/*First chamber*/
int boat;
int sceleton;
int rat;
/*Second chamber*/
int woman;
int bartender;
int priest;
/*Początek gry*/
int main(void) {
  cout << "********************************************************************"
          "***********\n"
          "___|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|____"
          "_|_____|_\n"
          "|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_"
          "____|____\n"
          "___|_____|_____|_____|_____|___██████████____|_____|_____|_____|____"
          "_|_____|_\n"
          "|_____|_____|_____|_____|____██████████████|_____|_____|_____|_____|"
          "_____|____\n"
          "___|_____|_____|_____|_____██████████████████|_____|_____|_____|____"
          "_|_____|_\n"
          "|_____|_____|_____|_____|__██████████████████___|_____|_____|_____|_"
          "____|____\n"
          "___|_____|_____|_____|_____██████████████████|_____|_____|_____|____"
          "_|_____|_\n"
          "|_____|_____|_____|_____|__██████████████████___|_____|_____|_____|_"
          "____|____\n"
          "___|_____|_____|_____|_____██████████████████|_____|_____|_____|____"
          "_|_____|_a\n"
          "/______/______/______/______/______/______/______/______/______/"
          "______/_____ /\n"
          "___/______/______/______/______/______/______/______/______/______/"
          "_____ /____\n"
          "/______/______/______/______/______/______/______/______/______/"
          "______/_____ /\n"
          "___/______/______/______/______/______/______/______/______/______/"
          "_____ /____\n"
          "********************************************************************"
          "***********\n";
  cout << "Welcome to the Treasure Dungeon\n";
  cout << "What's your name traveler?\n";
  player nm1;
  cin >> nm1.traveler;
  cout << "And what is your weapon?\n";
  cin >> nm1.weapon;
  cout << "You came across 2 paths.\n"
  "Which path you want to choose?\n"
  "First (press 1) is wet and slipery\n"
  "Second (press 2) looks pretty normal.\n";
  cin >> choice;
  /*Powtarzające się komnaty*/
  for (int powtorzenie=0; powtorzenie<2;powtorzenie++){
    switch (choice){
      /*Pierwszy zestaw*/
      case 1:
        for (int chamber=0; chamber<3;chamber++){
          int random = rand() % 3;
          if (random == 0){
              boatB();
              cin>>boat;
              if (boat==1){
                int chance = rand() % 5;
                if (chance == 0){
                  drowning();
                  cout<<"You lost "<<nm1.traveler<<" :(";
                  Sleep(90000);
                }
                else{
                  cout<<"'You managed to swim across the entire lake! Good Job "<<nm1.traveler<<"!!!";
                }
              }
              else {
                int chance = rand() % 5;
                if (chance==0){
                  boatR();
                  cout<<"You lost "<<nm1.traveler<<" :(";
                  Sleep(90000);
                  }    
                else{
                  cout<<"The stranger transported you and your "<< nm1.weapon <<" across the lake.";
                }
              }
            }
          else if (random == 1){
            sceletonE();
            cin>>sceleton;
              if (sceleton==1){
                int chance = rand() % 5;
                if (chance == 0){
                  sceletonF();
                  cout<<"You lost "<<nm1.traveler<<" :(";
                  Sleep(90000);
                }
                else{
                  cout<<"Good job "<<nm1.traveler<<" you managed to beat him with your "<<nm1.weapon<<"!";
                }
              }
              else{
                int chance = rand() % 5;
                if (chance == 0){
                  sceletonR();
                  cout<<"You lost "<<nm1.traveler<<" :(";
                  Sleep(90000);
                }
                else{
                  cout<<"Fortunately you managed to run away from him! Good Job "<<nm1.traveler<<"!!!";
                }
              }
          }
          else if (random == 2){
            ratE();
            cin>>rat;
            if (rat==1){
              int chance = rand() % 5;
              if (chance == 0){
                cout<<"When u were not watching the rat attacked you and he bit your carotid artery and you bled out. You are dead "<<nm1.traveler<<".\n";
                ratT();
                Sleep(90000);
              }
              else{
                cout<<"Rat named \"Grato\" happily join you! Now u have a comrade!";
              }
            }
            else{
              int chance = rand() % 5;
              if (chance == 0){
                cout<<"You ate him and u are feeling completly fine but that was not cool dude!";
              }
              else{
                cout<<"The rat was very sick and eating him poisoned you. You are dead "<<nm1.traveler<<". But honestlyyy... You deserved that.";
                ratP();
                Sleep(90000);
              }
            }   
          }
        }
        choice = 2;
        break;
      /*Drugi zestaw*/
      case 2:
      for (int chamber=0; chamber<3;chamber++){
          int random = rand() % 3;
          if (random == 0){
            womanE();
            cout<<"-Hey "<<nm1.traveler<<"! Come to me!\n"
            "Do you want to:\n"
            "(press 1) Come to her or (press 2) Run?\n";
            cin>>woman;
              if (woman==1){
                int chance = rand() % 5;
                if (chance == 0){
                  cout<<"The woman gave you a kiss and show you which path should you take. Nice.";
                }
                else{
                  cout<<"She was bloodthirsty vampire and she sucked all your blood. You are dead.";
                  vampireM();
                  Sleep(90000);
                }
              }
              else{
                int chance = rand() % 5;
                if (chance == 0){
                  cout<<"You were not capable of running away from her because she was a vampire. You are dead "<<nm1.traveler<<".";
                  vampireM();
                  Sleep(90000);
                }
                else{
                  cout<<"Fortunately you managed to run away from her! Good Job "<<nm1.traveler<<"!";
                }
              }
            }
          else if (random == 1){
            bartenderE();
            cin>>bartender;
              if (bartender==1){
                int chance = rand() % 5;
                if (chance==0){
                  bartenderP();
                  Sleep(90000);
                }
                else{
                  cout<<"The poison gave you additional vital forces! You are now super strong and super fast and you are able to see in dark";
                }
              }
              else{
                int chance = rand() % 5;
                if (chance==0){
                  bartenderD();
                  Sleep(90000);
                }
                else{
                  cout<<"The peddler droped in front of you. You decided to not drink it and went away";
                }
              }
          }
          else if (random==2){
            priestE();
            cin>>priest;
              if (priest==1){
                int chance = rand() % 5;
                if (chance == 0){
                  cout<<"Priest used his powers to defeat you. You are dead";
                  priestF();
                  Sleep(90000);
                }
                else{
                  cout<<"You menaged to beat him with your "<<nm1.weapon<<" and escaped safely! Fortunately!";
                }
              }
              else{
                int chance = rand() % 5;
                if (chance== 0){
                  cout<<"He managed to catch up with you. You are dead "<<nm1.traveler<<".";
                  priestF();
                  Sleep(90000);
                }
                else{
                  cout<<"You escaped! Congrats "<<nm1.traveler<<". You are fast.";
                }
              }
          }
      }
      choice = 1;
      break;
    }
  }
  cout<<"CONGRATULATIONS "<<nm1.traveler<<"!!!\n"
        "You managed to find the treasure.\n";
  treasure();
}