#include <iostream>

using namespace std;

int main()
{

    int a[3] = {17, 28, 30}, b[3] = {99, 16, 8}, alice = 0, bob = 0;

    for (int i = 0; i < 3; i++)
    {
        if (a[i] > b[i])
            alice++;

        if (a[i] < b[i])
            bob++;
    }

    cout << "Point of Alice is : " << alice << endl;
    cout << "Point of bob is : " << bob;

    return 0;
}