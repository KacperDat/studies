#include "function.h"
#include <iostream>
#include <cmath>

using namespace std;

void VehicleInspection::checking_brakes(float left_break, float right_break) {
    if (left_break > 50 || right_break > 50) {
        cout << "the brakes work well" << endl;
    } else if (fdim(left_break, right_break) < 30 || fdim(right_break, left_break) < 30) {
        cout << "the brakes work well" << endl;
    } else {
        cout << "the brakes are faulty" << endl;
    }
}

void VehicleInspection::checking_shock_absorbers(float left_shock_absorber, float right_shock_absorber) {
    if (left_shock_absorber > 40 || right_shock_absorber > 50) {
        cout << "the shock absorbers work well" << endl;
    } else if (fdim(left_shock_absorber, right_shock_absorber) < 30 ||
               fdim(right_shock_absorber, left_shock_absorber) < 30) {
        cout << "the shock absorbers work well" << endl;
               } else {
                   cout << "the shock absorbers are faulty" << endl;
               }
}

