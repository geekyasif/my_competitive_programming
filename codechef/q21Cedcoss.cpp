#include <iostream>
#include <cstring>

using namespace std;

bool checkStr(string str, int strEnd)
{
    int prev = 0;
    bool result = true;
    for (int i = 0; i <= strEnd; i++)
    {
        if (str[i] == '+' && str[strEnd] == '+')
        {
            prev = i;
        }
        else
        {
            if (i == strEnd)
            {
                result = true;
            }
            else if (str[prev] == '+' && str[i + 1] == '+')
            {
                result = true;
            }
            else
            {
                return false;
            }
        }
    }

    return result;
}

int main()
{

    string str = "++d+===+c++==a";

    int strEnd = str.length() - 1;

    if (checkStr(str, strEnd))
    {
        cout << "Satisfied" << endl;
    }
    else
    {
        cout << "Not Satisfied" << endl;
    }

    return 0;
}