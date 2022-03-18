#include <iostream>
#include <cstring>
using namespace std;

int main()
{

    int t;
    cin >> t;
    while (t--)
    {
        int n;
        unsigned long long int fact = 1;
        cin >> n;
        while (n != 0)
        {
            fact = fact * n;
            n--;
        }
        cout << fact << endl;
    }

    return 0;
}