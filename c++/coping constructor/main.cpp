#include <iostream>
using namespace std;
class Car {
private:
    string mark;
    string model;
    float combustion;
public:

    Car(string p_mark="uknown", string p_model="unknown", float p_combustion=0)
    : mark(p_mark), model(p_model), combustion(p_combustion) {}
    Car(const Car &p_car)
        :mark(p_car.mark), model(p_car.model), combustion(p_car.combustion){}
    void display() {
        cout << "mark: " << mark << endl;
        cout << "model: " << model << endl;
        cout << "combustion: " << combustion << endl;
    }
};
int main() {
    Car car1("Audi","A4",9);
    Car car2=car1;
    car2.display();


    return 0;
}