#include<iostream>
using namespace std;

int main(){
	long long n;
	cin>>n;	
	long long h=n;
	long long k = (n-1)%2027 ;
	long long k1;
	if(n%2==0){
		k1 = ((n/2)%2027)*((n+1)%2027);
	}else{
		k1 = ((n)%2027)*(((n+1)/2)%2027);
	}
	k = k*(k1%2027);

	cout<<((h%2027)+(k%2027))%2027;
}
