#include <iostream>
#include "Words.h"
#include "Numbers.h"

using namespace std;
void Numbers:: setNumber(int p_number) {
    number = p_number;
}
void Numbers:: printNumber() {
    cout <<"your number: "<< number << endl;
}