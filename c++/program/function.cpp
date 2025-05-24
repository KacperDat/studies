#include <iostream>
#include "file.hpp"

using namespace std;
void Car::enter_car_information(){

cout<<"enter_brand"<<endl;
    cin>>brand;
    cout<<"enter_model"<<endl;
    cin>>model;
    cout<<"enter_combustion"<<endl;
    cin>>combustion;
}
void Car::data_show() {
    cout<<brand<<endl;
    cout<<model<<endl;
    cout<<combustion<<endl;

}