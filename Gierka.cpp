#include <iostream>
#include "sceletonF.cpp"
#include "sceletonR.cpp"
#include "vampireM.cpp"
#include "boatB.cpp"
using namespace std;
class player {
public:
  string traveler = "";
  string weapon = "";
};
int choice;
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
  for (int powtorzenie=0; powtorzenie<2;powtorzenie++){
    switch (choice) {
      case 1:
        boatB();
        choice=2;
        break;
      case 2:
        
        choice=1;
        break;
  
    }
  }
}