#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

// Checking palindrome without using recursion
bool CheckPalindromeWithoutRecurion(string a)
{
    for (int i = 0; i < a.length(); i++)
    {

        if (a[i] != a[(a.length() - 1) - i])
        {
            return false;
        }
    }

    return true;
}

// Checking palindrome  using recursion
bool CheckPalindromeWithRecurion(string str)
{

    if (str.length() == 0 || str.length() == 1)
    {
        return true;
    }

    if (str[0] == str[str.length() - 1])
    {
        return CheckPalindromeWithRecurion(str.substr(1, str.length() - 1));
    }

    return false;
}

int main()
{

    string a = "abba";

    // calling function without recursion
    if (CheckPalindromeWithoutRecurion(a))
    {
        cout << "Palindrome without recursion  " << endl;
    }
    else
    {
        cout << "Not Palindrome without recursion" << endl;
    }

    // calling function with recursion
    if (CheckPalindromeWithRecurion(a))
    {
        cout << "Palindrome with recursion" << endl;
    }
    else
    {
        cout << "Not Palindrome with recursion" << endl;
    }

    return 0;
}