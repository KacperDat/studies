
#include "Numbers.h"
#include "Words.h"
#include <iostream>
using namespace std;


int main() {
Words w1;
    Numbers n2;
    w1.setWord("Hello world");
    n2.setWord("Audi");
    w1.printWord();
    n2.printWord();
    n2.setNumber(1234);
    n2.printNumber();




    return 0;

}
