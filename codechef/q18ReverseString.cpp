
#include <iostream>
#include <cstring>
using namespace std;

string revStrWithRecursion(string a)
{

    if (a == "")
    {
        return "";
    }

    return revStrWithRecursion(a.substr(1)) + a[0];
}

string revStrWithoutRecursion(string str)
{
    string reverseStr = "";
    for (int i = 0; i < str.length(); i++)
    {
        reverseStr = str[i] + reverseStr;
    }
    return reverseStr;
}
int main()
{
    string a = "asif";
    string c = revStrWithoutRecursion(a);
    cout << "Reverse without recursion : " << c << endl;
    string d = revStrWithRecursion(a);
    cout << "Reverse with recursion : " << d << endl;
}
