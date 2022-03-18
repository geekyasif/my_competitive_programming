// Write	a	program	to	remove	Duplicate	characters	from	the	String.

#include <iostream>
#include <string>
using namespace std;

string remDuplicate1(string str)
{
    string a = "";
    bool count = true;
    for (int i = 0; i < str.length(); i++)
    {

        if (a.length() == 0)
        {
            a = a + str[i];
        }
        else
        {

            for (int j = 0; j < a.length(); j++)
            {
                if (str[i] == a[j])
                {
                    count = false;
                    break;
                }
            }

            if (count)
            {
                a = a + str[i];
            }
        }
    }
    return a;
}

int main()
{

    string str = "asifmohammaad";
    cout << remDuplicate1(str) << endl;

    return 0;
}