#include <iostream>

using namespace std;
class Car
{
private:
    string brand;
    string model;
    float combustion;
public:
    /* void enter_car_information()
     {
         count<<"your car brand"<<endl;
         cin>>brand;
         count<<"your car model"<<endl;
         cin>>model;
         count<<"your car combustion"<<endl;
         cin combustion;
     }
     void data_details()
     {
         cout<<"brand: "<<brand<<endl;
         cout<<"model: "<<model<<endl;
         cout<<"combustion: "<<combustion<<endl;

     }*/
 void data_details();
 void enter_car_information();

};
void Car::enter_car_information()
{
    cout<<"your car brand"<<endl;
    cin>>brand;
    cout<<"your car model"<<endl;
    cin>>model;
    cout<<"your car combustion"<<endl;
    cin>>combustion;
}
void Car::data_details()
     {
         cout<<"brand: "<<brand<<endl;
         cout<<"model: "<<model<<endl;
         cout<<"combustion: "<<combustion<<endl;

     }
int main()
{
    Car car_1;
    Car car_2;
    car_1.enter_car_information();
    car_1.data_details();
    return 0;
}
