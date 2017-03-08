#include <iostream>
#include <cstdlib>

using namespace std;

int successor(int number) {
    return number + 1;
}

double successor(double number) {
    return number + 1;
}

int main() {
    cout << successor(10) << endl;
    cout << successor(10.3) << endl;

    return 0;
}

