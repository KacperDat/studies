#include <iostream>
using namespace std;
class Bike {
    private:
    string name;
    string color;
    int age;
    public:
    Bike() {
        name ="not specified";
        color="not specified";
        age=0;
    }
    void set_data() {
        cout<<"Enter name: "<<endl;
        cin>>name;
        cout<<"Enter color: "<<endl;
        cin>>color;
        cout<<"Enter age: "<<endl;
        cin>>age;

    }
    void display() {
        cout<<"Name: "<<name<<endl;
        cout<<"Color: "<<color<<endl;
        cout<<"Age: "<<age<<endl;
    }
};
int main() {
Bike b1,b2;
    b1.set_data();
b1.display();
    b2.display();

    return 0;
}