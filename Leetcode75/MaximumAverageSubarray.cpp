#include <iostream>
#include <vector>
using namespace std;


double findMaxAverage(vector<int>& nums, int k) {
    double maxSumKNum= 0 ;
    double sumKNum = 0;
    for(int i =0;i<k;i++)  {
        sumKNum+=nums[i];
    }
    maxSumKNum = sumKNum;
    for(int i=1;i<=nums.size()-k;i++){
        sumKNum = sumKNum-nums[i-1]+nums[i-1+k];
        maxSumKNum = max(maxSumKNum,sumKNum);
    }


    return maxSumKNum/k ;
}
int main(){
    vector<int> nums = {5};
    int k =1;

    cout<<"averagen : "<<findMaxAverage(nums,k);

}