// Final Value of Variable After Performing Operations
#include <iostream>
#include <cstring>
#include <vector>
using namespace std;

int Cal(string *a)
{
    int count = 0;
    int i = 0;
    while (a != nullptr)
    {
        if (a[i] == "--X" || a[i] == "X--")
        {
            count = count - 1;
            cout << count << endl;
        }

        else
        {
            count = count + 1;
            cout << count << endl;
        }
        i++;
    }
    cout << "\nResult before send is : " << count;
    return count;
}

int vectorFunction(vector<string> &operations)
{
    int count = 0;
    for (int i = 0; i < operations.size(); i++)
    {
        if (operations[i] == "--X" || operations[i] == "X--")
        {
            count = count - 1;
        }

        else
        {
            count = count + 1;
        }
    }
    return count;
}

int main()
{

    // string a[3] = {"++X", "++X", "X++"};
    // int count = Cal(a);
    // cout << "\nResult is" << count;

    // vector<string> operations = {"X++", "++X", "--X", "X--"};
    // int count = vectorFunction(operations);
    // cout << count;
    string a = "Asig";
    a + "Mohammad";
    cout << a << endl;
}
