//Includes
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <string.h>
using namespace std;


//Constants
const int SIZE = 10;

//Function declarations
void basic_syntax();
char* pointers(char* word, char* substring);
void programming();

//MAIN
int main(int argc, char *argv[]) {
    if (argc > 1) {
        cerr << "ERROR: No arguments expected.\n";
        exit(EXIT_FAILURE);
    }
    char word[8] = {'b', 'a', 's', 'e', 'b', 'a', 'l', 'l'};
    char sub[4] = {'b', 'a', 'l', 'l'};
    cout << pointers(word, sub) << endl;
    return 0;
}

//FUNCTIONS
void basic_syntax() {
    string hold;
    cout << "Enter" << " " << "a word: ";
    cin >> hold;
    for (int i = 0; i < hold.length(); i++) {
        cout << hold[i] << endl;
    }
}

char* pointers(char* word, char* substring) {
    cout << *word << " " << *substring << endl;
    int word_len = sizeof(*word)/sizeof(char);
    int sub_len = sizeof(*substring)/sizeof(char);
    cout << word_len << " " << sub_len << endl;
    if (word_len <= sub_len) {
        return word;
    }

    while (word_len > sub_len) {
        pointers(word+1, substring);
    }
}

void programming() {

}