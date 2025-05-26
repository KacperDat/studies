#include <iostream>
using namespace std;
class Car {
private:
    string mark="unknown";
    string model="uknown";
    float combustion=0;
    public:
    Car()
    :Car{"uknown","uknown",0}{}
    Car(string p_mark)
    :Car{p_mark,"uknown",0}{}
    Car(string p_mark, string p_model)
    :Car{p_mark,p_model,0}{}
    Car(string p_mark, string p_model, float p_combustion): mark(p_mark), model(p_model), combustion(p_combustion) {}
    void display() {
        cout << "mark: " << mark << endl;
        cout << "model: " << model << endl;
        cout << "combustion: " << combustion << endl;
    }
};
int main() {
   Car car1;
    Car car2("Audi");
    Car car3("Audi", "A4");
    Car car4("Audi", "A5",7);
    car1.display();
    car2.display();
    car3.display();
    car4.display();

    return 0;
}