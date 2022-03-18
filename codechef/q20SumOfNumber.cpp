#include <iostream>

using namespace std;

int SumOfNumberWithRecursion(int num)
{

    if (num <= 1)
    {
        return 1;
    }

    return SumOfNumberWithRecursion(num - 1) + num;
}

int SumOfNumberWithoutRecursion(int num)
{
    // with formula
    // return num * (num + 1) / 2;

    // without formula
    int result = 0;
    for (int i = 1; i <= num; i++)
    {
        result += i;
    }

    return result;
}

int main()
{

    int num = 5;
    int result = SumOfNumberWithoutRecursion(num);
    cout << "Sum of number without recursion is : " << result << endl;
    int result2 = SumOfNumberWithRecursion(num);
    cout << "Sum of number with recursion is : " << result2 << endl;

    return 0;
}