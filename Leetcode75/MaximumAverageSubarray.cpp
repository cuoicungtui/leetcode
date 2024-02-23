#include <iostream>
#include <vector>
using namespace std;


double findMaxAverage(vector<int>& nums, int k) {
    ios::sync_with_stdio(false);
    double sumKNum = 0;
    for(int i =0;i<k;i++)  {
        sumKNum+=nums[i];
    }
    double maxSumKNum = sumKNum;
    for(int i=1;i<=nums.size()-k;i++){
        sumKNum = sumKNum-nums[i-1]+nums[i-1+k];
        maxSumKNum = std::max(maxSumKNum,sumKNum);
    }


    return maxSumKNum/k ;
}
int main(){
    vector<int> nums = {5};
    int k =1;

    cout<<"averagen : "<<findMaxAverage(nums,k);

}