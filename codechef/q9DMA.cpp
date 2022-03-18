#include <iostream>

using namespace std;

int main()
{

    int n;

    cin >> n;
    // int *arr = new int[n];
    int arr[n];

    for (int i = 0; i < n; i++)
    {
        int a;
        cin >> a;
        arr[i] = a;
    }

    for (int j = 0; j < n; j++)
    {
        cout << arr[j] << " ";
    }

    return 0;
}