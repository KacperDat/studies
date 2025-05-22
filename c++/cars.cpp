#include <iostream>
#include <cmath>
using namespace std;
class  Car
{
public:
    string brand;
    string model;
    float combustion;
    void cost_of_fuel(float combustion){
    float price_of_fuel = 6.54;
    cout<<"cost of fuel: "<<round(price_of_fuel*combustion*100)/100<<endl;

    }

};
int main()
{
    Car car_1;
    Car car_2;
car_1.brand ="Audi";
car_1.model="A4";
car_1.combustion=8.5;
car_1.cost_of_fuel(car_1.combustion);

car_2.brand ="BMW";
car_2.model="e46";
car_2.combustion=12.3;
car_2.cost_of_fuel(car_2.combustion);

    return 0;
}
