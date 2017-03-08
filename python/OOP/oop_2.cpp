#include <iostream>
using namespace std;

int f(int n);
int f(int n, int m);

int main() {
    cout << "f(3): " << f(3) << endl;
    cout << "f(3, 4): " << f(3, 4) << endl;

    return 0;
}

int f(int n) {
    return n + 42
}

int f(int n, int m) {
    return n + m + 42;
}

