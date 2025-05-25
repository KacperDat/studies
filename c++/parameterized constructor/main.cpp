#include <iostream>

using namespace std;
class Bike {
private:
    string name;
    string color;
    int age;
    public:
    Bike() {
        name = "unkown";
        color = "unknow";
        age = 0;
    }
    Bike(string p_name, string p_color, int p_age) {
        name = p_name;
        color = p_color;
        age = p_age;
    }

    void display() {
        cout << "Name: " << name << endl;
        cout << "Color: " << color << endl;
        cout << "Age: " << age << endl;

    }
};
int main() {
    Bike b_0,b_1("cross","yellow",3),b_2("delta","green",7);
b_1.display();
    b_2.display();
    b_0.display();



    return 0;
}