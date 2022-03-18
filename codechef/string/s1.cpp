#include <iostream>
#include <string>
using namespace std;

int main()
{

    string s = "asifmohammaad";
    int count = 0;
    for (int i = 0; i < s.length(); i++)
    {
        for (int j = 0; j < s.length(); j++)
        {
            if (s[j] == s[i])
            {
                count++;
            }
        }
        cout << "Number of " << s[i] << " is " << count << endl;
        count = 0;
    }

    return 0;
}