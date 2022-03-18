#include<iostream>
using namespace std;

int main(){
	int t;
	cin>>t;
	while(t--){
		int n, rem,totalOccurences = 0;
		cin>>n;
		while(n != 0){
		    rem = n % 10;

			if( rem == 4)
                totalOccurences += 1;

            n = n/10;
		}
		cout<<totalOccurences<< endl;
	}

	return 0;
}
