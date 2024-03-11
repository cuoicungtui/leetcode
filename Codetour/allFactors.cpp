#include<iostream>
#include<cmath>
#include <vector>
using namespace std;

vector<int> allFactors(int A) {
    vector<int> factorsOfA;
    for(int i=1;i<=sqrt(A);i++){
        if(A%i==0){
            factorsOfA.push_back(i);
        }       
    }
    if(A>1){
    	for(int i=factorsOfA.size()-1;i>=0;i--){
        	factorsOfA.push_back(A/factorsOfA[i]);
    	}
    	
	}
	
   
    
    return factorsOfA;
    
}

int main(){
	int n;
	cin>>n;	
	vector<int> factorList = allFactors(n);
	for (int i = 0;i< factorList.size();i++) {
        cout << factorList[i] << " ";
    }
}
