#include<iostream>

using namespace std;

int main(){
	int n, total = 0;
	long k, input;
	
	cin>>n>>k;
	for(int i = 0 ; i < n; i++){
		cin>>input;
		if(input % k == 0) {
			total += 1;
		}
	}
	cout<<total;
	
}

