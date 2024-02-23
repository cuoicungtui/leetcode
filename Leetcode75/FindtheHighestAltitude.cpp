#include<iostream>
#include<vector>
using namespace std;

int largestAltitude(vector<int>& gain) {
    int hight = 0;
    int max_hight = 0;
    for(auto i:gain){
        hight = hight+i;
        max_hight = max(max_hight,hight);
    }
    return max_hight;

}

int main(){
    vector<int> gain = {-5,1,5,0,-7};
    cout<< largestAltitude(gain);
}