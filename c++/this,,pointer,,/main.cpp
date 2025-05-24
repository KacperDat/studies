#include <iostream>
using namespace std;
class PointerThis {
private:
    int number;
public:
    void set_number(int p_number) {
        this->number = p_number;
    }
    void display_number() {
        cout<<"number: "<<number<<endl;
    }
};
int main() {
    PointerThis p1;
    PointerThis p2;
    p1.set_number(10);
    p2.set_number(20);
    p1.display_number();
    p2.display_number();
    return 0;
}