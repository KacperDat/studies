

#include "Words.h"
#include <iostream>
using namespace std;
void   Words::setWord(string p_word) {
    word = p_word;
}
void Words::printWord() {
    cout <<"your word: "<< word << endl;
}
