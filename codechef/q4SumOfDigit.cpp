#include<iostream>
using namespace std;

int main(){
	
	int t, n, sum = 0, rem;
	
	cin>>t;
	while(t--){
		cin>>n;
		while(n--){
			rem = n % 10;
			sum = sum + rem;
			n = n / 10;
		}
		cout<<sum<<endl;
	}
}
