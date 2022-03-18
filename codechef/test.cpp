// #include <iostream>
// #include <iomanip>
// using namespace std;

// float cashProcess(int input, float *totalBalance, float charge)
// {
//     if (input % 5 == 0 && input <= *totalBalance)
//     {
//         float totalAmountToBeDebited = input + charge;
//         *totalBalance = *totalBalance - totalAmountToBeDebited;
//         return *totalBalance;
//     }
//     else
//     {
//         return *totalBalance;
//     }
// }

// int main()
// {

//     int input;
//     float totalBalance;
//     float charge = 0.50;

//     cin >> input;
//     cin >> totalBalance;

//     int avlAmount = cashProcess(input, &totalBalance, charge);
//     cout << setprecesion(2) << totalBalance;

//     return 0;
// }

#include <iostream>

using namespace std;

int fun2(int a)
{
    if (a == 10)
        return a;

    return a + fun2(a + 1);
}

int main()
{

    cout << fun2(6);
    return 0;
}

// ---------------------------------- recursion problem-------------------------------------------------------------

// int fun1(int x, int y)
// {
//     if (x == 0)
//         return y;
//     else
//         return fun1(x - 1, x + y);
// }

// /* Assume that n is greater than or equal to 1 */
// int fun1(int n)
// {
//     if (n == 1)
//         return 0;
//     else
//         return 1 + fun1(n / 2);
// }

// /* Assume that n is greater than or equal to 0 */
// void fun2(int n)
// {
// if(n == 0)
//     return;

// fun2(n/2);
// cout << n%2 << endl;
// }

// void fun1(int n)
// {
//    int i = 0;
//    if (n > 1)
//      fun1(n - 1);
//    for (i = 0; i < n; i++)
//      cout << " * ";
// }

// #define LIMIT 1000
// void fun2(int n)
// {
//   if (n <= 0)
//      return;
//   if (n > LIMIT)
//     return;
//   cout << n <<" ";
//   fun2(2*n);
//   cout << n <<" ";
// }