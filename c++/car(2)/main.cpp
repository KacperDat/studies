#include <iostream>

using namespace std;
class Car
{
private:
    string brand;
    string model;
    float combustion;
public:
    /* void enterYourDetails()
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
     }; */
     void setBrand(string p_brand){brand=p_brand;}
     void setModel(string p_model){model=p_model;}
     void setcombustion(float p_combustion){combustion=p_combustion;}
     string getBrand(){return brand;}
     string getModel(){return model;}
     float getCombustion(){return combustion;}
     };
    int main()
    {
        Car car_1;
        Car car_2;
        car_1.setBrand("Audi");
        car_1.setModel("A4");
        car_1.setcombustion(9);
        cout<<car_1.getBrand()<<endl;
         cout<<car_1.getModel()<<endl;
          cout<<car_1.getCombustion()<<endl;
        /*   cout<<"car 1:"<<endl;
           car_1.enterYourDetails();
           car_1.dataDisplay();
           cout<<"car 2:"<<endl;
           car_2.enterYourDetails();
           car_2.dataDisplay();*/


        return 0;
    }
