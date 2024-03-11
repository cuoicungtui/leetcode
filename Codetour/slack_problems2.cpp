#include<iostream>
#include <map>
#include <string>
using namespace std;

int main(){
	string s;
	cin>>s;
	

	
	map<char, int>table;
	for(int i = 0;i<s.length();i++){
		char a = s[i];
		if(table.find(a) != table.end()){
			table[a]+=1;
		}else{
			table[a]=1;
		}
		
	}
	
	int cout[9];
	for (int i=1;i<=9;i++)
		cout[i]=0;
	
	if(table.find('w') != table.end()){
		cout[2] = table['w'];
		table['w'] = 0;
		table['t'] -= table['w'];
		table['t'] -= table['w'];
		
	}
	if(table.find('g') != table.end()){
		cout[8] = table['g'];
	}
	if(table.find('x') != table.end()){
		cout[6] = table['x'];
	}
	


		
	
}
