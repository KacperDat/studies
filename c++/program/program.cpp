#include <iostream>
#include "file.hpp"

using namespace std;
int main() {
Car car_1;
    Car car_2;
    car_1.enter_car_information();
    car_2.enter_car_information();
    cout<<endl;
    car_1.data_show();
    car_2.data_show();


    return 0;
}