#include <iostream>
#include <string>
using namespace std;
int main()
{
    int a = 40;
    // cout << "Printing the address of a is : " << &a;
    int &addressOfA = a;
    addressOfA = 30;
    cout << "Address of a is " << &a << endl;
    cout << "&addressOf a value " << &addressOfA << "\n addressOfA is  " << addressOfA;
    // cout << "*ptr valiue: " << *ptr << "\n Ptr " << ptr;
    // cout << "\nAddress of a: " << &addressOfA << " and  value after change is " << addressOfA << endl;
    // int arr[] = {1, 2, 3, 4, 5, 6};
    // cout << "Array conting the address of first element : " << arr << endl;
    // int *arrptr = arr;
    // cout << "*arrptr is " << *arrptr + 4 << "\n value of arrptr is " << arrptr << endl;

    // void *ptrString;
    // string asif = "asif";
    // ptrString = &asif;
    // cout << *ptrString;
    // int lengthOfArr = sizeof(arr) / sizeof(int) - 1;
    // for (int i = 0; i <= lengthOfArr; i++)
    // {
    //     // cout << ptr[i] << endl;
    // }
}