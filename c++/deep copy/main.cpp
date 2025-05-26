#include <iostream>
using namespace std;
class Car {
private:
    string brand;
    string model;
    float *combustion;
public:
    Car() {
        combustion = new float;
    }
    Car(const Car &object) {
        brand = object.brand;
        model = object.model;
        combustion = new float;
        *combustion = *(object.combustion);
    }
    void car_information(string p_brand,string p_model,float p_combustion) {
        brand = p_brand;
        model = p_model;
        combustion = new float;
        *combustion = p_combustion;
    }
    void data_display() {
        cout << "Brand: " << brand << endl;
        cout << "Model: " << model << endl;
        cout << "Combustion: " << *combustion << endl;
    }
    ~Car() {
        delete combustion;
    }
};
int main() {
    Car car_1;
    car_1.car_information("Audi","A4",8);
    car_1.data_display();
    Car car_2(car_1);
    car_2.data_display();


    return 0;
}