#include <iostream>
using namespace std;

bool IsSubsequence(string s, string t){

    int index_s = 0;
    int index_t = 0;
    if(t.size()<s.size()) return false;
    // if (s.size()==0) return true;

    while (index_t < t.size() && index_s < s.size())
    {
        if(s[index_s]==t[index_t]){
            index_s += 1;
        }
        
        index_t+=1;
    }
    
    return index_s == s.size();
}



int main(){
    string str1 = "axc" ;
    string str2 = "ahbgdc" ;
    cout<<IsSubsequence(str1,str2);
}