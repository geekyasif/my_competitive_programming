#include <iostream>
using namespace std;

int main()
{

    long long int arr[5] = {1000000001, 1000000002, 1000000003, 1000000004, 1000000005};
    long long int sum = 0;

    for (long long int i = 0; i < 5; i++)
    {
        sum = sum + arr[i];
    }

    cout << sum;

    return 0;
}
