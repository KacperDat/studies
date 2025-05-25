#include <iostream>
using namespace std;
class Car {
    public:
    string *brand;
    string *model;
    float *combustion;
        Car() {
            cout << "car constructor" << endl;
            brand = new string;
            model = new string;
            combustion = new float;
            cout << "dynamic memory allocation" << endl;
        }
        ~Car() {
            delete brand, model, combustion;
            cout << "car destructor" << endl;
        }

};


int main() {
    Car car_1,car_2;


    return 0;
}