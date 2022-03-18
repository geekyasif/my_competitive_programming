#include <iostream>
#include <iomanip>

using namespace std;

int main()
{

    int arrLen;

    float pos = 0, neg = 0, zero = 0;

    cin >> arrLen;
    int arr[arrLen];

    for (int i = 0; i < arrLen; i++)
    {
        int num;
        cin >> num;
        arr[i] = num;

        if (arr[i] > 0)
            pos++;

        if (arr[i] < 0)
            neg++;

        if (arr[i] == 0)
            zero++;
    }

    cout << "value of pos : " << setprecision(6) << pos / arrLen << endl;
    cout << "value of neg : " << setprecision(6) << neg / arrLen << endl;
    cout << "value of zero : " << setprecision(6) << zero / arrLen << endl;

    return 0;
}