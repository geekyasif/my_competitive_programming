#include <iostream>
#include <string>
using namespace std;

string ConvertToBinaryWithoutRecursion(int decimal)
{
    string binary = "";
    while (decimal != 0)
    {
        int rem = decimal % 2;
        binary = to_string(rem) + binary;
        decimal = decimal / 2;
    }

    return binary;
}

string ConvertToBinaryWithRecursion(int decimal)
{

    if (decimal == 0)
    {
        return "";
    }

    return ConvertToBinaryWithRecursion(decimal / 2) + to_string(decimal % 2);
}

int main()
{

    int decimal = 8;
    cout << ConvertToBinaryWithoutRecursion(decimal) << endl;
    cout << ConvertToBinaryWithRecursion(decimal) << endl;

    return 0;
}