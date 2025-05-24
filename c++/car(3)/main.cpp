#include <iostream>

using namespace std;
class Information
{
protected:
    string brand;
    string model;
    float combustion;
};
class Car: Information{
public:
    void enterYourDetails()
     {
         cout<<"enter car brand: "<<endl;
         cin>>brand;
         cout<<"enter car model: "<<endl;
         cin>>model;
         cout<<"enter  car combustion :"<<endl;
         cin>>combustion;
     }
     void dataDisplay()
     {
         cout<<"car brand: "<<brand<<endl;
         cout<<"car model: "<<model<<endl;
         cout<<"car combustion: "<<combustion<<endl;

     }


     };
    int main()
    {
        Car car_1;
        Car car_2;
       cout<<"first car"<<endl;
       car_1.enterYourDetails();
       cout<<"second car"<<endl;
       car_2.enterYourDetails();
       car_1.dataDisplay();
       car_2.dataDisplay();

        return 0;
    }
