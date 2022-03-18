#include <bits/stdc++.h>

using namespace std;

int main()
{

    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        long long int fact = 1;
        while (n != 0)
        {
            fact = fact * n;
            n--;
        }
        cout << fact << endl;
    }

    return 0;
}

// #include <bits/stdc++.h>

// using namespace std;

// long long int fact(int n)
// {
//     if (n == 1 || n == 0)
//     {
//         return 1;
//     }

//     return fact(n - 1) * n;
// }

// int main()
// {

//     int t;
//     cin >> t;
//     while (t--)
//     {
//         int n;
//         cin >> n;

//         long long int smallFact = fact(n);
//         cout << smallFact << endl;
//     }

//     return 0;
// }
