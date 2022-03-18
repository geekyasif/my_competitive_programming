#include <iostream>
#include <cstdlib>

using namespace std;

int main()
{

    int m, n;
    cin >> m >> n;
    int arr[m][n];

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            int num;
            cin >> num;
            arr[i][j] = num;
        }
    }

    int d1 = 0, d2 = 0;
    for (int i = 0; i < m; i++)
    {
        for (int j = i; j <= i; j++)
        {
            cout << arr[i][j] << " " << endl;
            d1 = d1 + arr[i][j];
            d2 = d2 + arr[i][m - 1 - j];
        }
    }

    cout << "Sum is : " << d1 << " " << d2 << endl;
    cout << "Diagonal Difference is " << abs(d1 - d2);

    return 0;
}
