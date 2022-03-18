#include <iostream>
#include <string>
using namespace std;

int main()
{

    string s = "asif mohammaad";
    string a = "";
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] != ' ')
        {
            a = a + s[i];
        }
    }
    cout << a;

    return 0;
}