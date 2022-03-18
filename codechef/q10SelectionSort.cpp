#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{

    int t;
    cin >> t;
    long long int arr[t];

    for (int i = 0; i < t; i++)
    {
        cin >> arr[i];
    }

    for (int i = 0; i < t; i++)
    {
        for (int j = 0; j < 5 - 1; j++)
        {
            long long int temp;
            if (arr[j] > arr[j + 1])
            {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
    // sort(arr, arr + t);

    for (int x : arr)
    {
        cout << x << endl;
    }

    return 0;
}