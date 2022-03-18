#include <iostream>

using namespace std;

int main()
{

    int arrLength, sum = 0;
    ;
    cout << "Enter the length of arr : ";
    cin >> arrLength;

    int arr[arrLength];
    for (int i = 0; i < arrLength; i++)
    {
        int num;
        cin >> num;
        arr[i] = num;
    }

    while (arrLength--)
    {
        sum = sum + arr[arrLength];
    }

    cout << sum;

    return 0;
}