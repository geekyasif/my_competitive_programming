#include<iostream>
using namespace std;

int main(){
	int t;
	cin>>t;
	while(t--){
		int a, last,first;
		cin>>a;
		last = a%10;
		while(a != 0){
		    first = a % 10;
			a = a/10;
		}
		cout<< last + first<< endl;
	}

	return 0;
}
