#include <iostream>
#include "function.h"

using namespace std;

int main() {
    VehicleInspection inspection;
    inspection.checking_brakes(55, 60);
    inspection.checking_shock_absorbers(45, 43);
    return 0;
}
