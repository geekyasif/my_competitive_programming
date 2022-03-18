// Write a Code to check whether one string is a rotation of another
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

bool checkStringRotation(string str1, string str2)
{
    string str3 = str1;
    if (str2.length() > str3.length())
    {
        return false;
    }
    else
    {
        int i = 0, j = 0;
        while ((str2[i] != '\0') || (str3[j] != '\0'))
        {
            if (str2[i] != str3[j])
            {
                j++;
                i = 0;
            }
            else
            {
                j++;
                i++;
            }
        }
        cout << i << endl;
        return true;
    }
}

int main()
{
    string str1 = "geeksaforgeeks";
    string str2 = "for";
    // if (checkStringRotation(str1, str2))
    // {
    //     cout << "true";
    // }
    // else
    // {
    //     cout << "false";
    // }

    cout << suffle(1, 10);

    return 0;
}