#include <iostream>

using namespace std;

void asc(int start, int end, int *arr)
{

    for (int i = start; i <= end; i++)
    {
        for (int j = 0; j < end - i; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;

                cout << temp << endl;
                cout << arr[j] << endl;
                cout << arr[j + 1] << endl;
            }
        }
    }
}

void desc(int start, int end, int *arr)
{

    for (int i = start; i <= end; i++)
    {
        for (int j = start; j < end - i; j++)
        {
            if (arr[j] < arr[j + 1])
            {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

void greatestNum(int start, int end, int *arr)
{
    int greatest = 0;
    for (int i = start; i < end; i++)
    {
        if (greatest < arr[i])
        {
            greatest = arr[i];
        }
    }

    cout << "Greatest Number is : " << greatest << endl;
}

void display(int *arr)
{

    for (int i = 0; i < 9; i++)
    {
        cout << " " << arr[i];
    }
}

int main()
{

    int arr[9] = {6, 1, 9, 8, 4, 2, 5, 3, 7};

    asc(0, 2, arr);
    desc(6, 8, arr);
    greatestNum(3, 5, arr);
    display(arr);

    return 0;
}