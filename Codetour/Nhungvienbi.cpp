#include<iostream>
#include <cstdlib>
#include <bits/stdc++.h>
using namespace std;


int main(){
	ios_base::sync_with_stdio(false); 
    cin.tie(0);

	int N; long X;
	cin>>N>>X;
	long A[N];
	for (int i=0;i<N;i++){
		cin>>A[i];
	};
	long absarr[N-1];
	for (int i=0;i<N-1;i++){
		absarr[i] = abs(A[i] - A[i+1]);
	};

	int count = 0;
	
	for(int i=0;i<N-1;i++){
		long long sum = absarr[i] ;
		int difference = 1;
		int index = i+1;
		while(sum*difference < X  ){

		};
		count += (N-index);
	};
	
	cout<<count<<endl;
		
}
