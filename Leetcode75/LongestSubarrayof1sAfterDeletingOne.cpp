#include<iostream>
#include<vector>
using namespace std;

int longestSubArray(vector<int>& nums){
    int count1 = 0;
    int count2 = 0;
    int maxCount = 0;
    int start = 0;
    bool check0 = false;
    bool start_new = false;
    int start_new_index = 0;
    while(nums[start]==0){
        start++;
    }
    for(int i = start+1;i<nums.size();i++){
        if(nums[i]==0){
            if(check0 ==false){
                count1 = (i -start);
                check0 = true;
                start_new = true;
            }else{
                check0 = false;
                count2 = i-start;
                maxCount = max(maxCount,(count1+count2));
                count1 = count2;
                start = start_new_index;
            }

        }else{
            if(start_new){
                start_new_index = i;
                start_new = false;
            }
        }
          

    }

    if(nums[nums.size()-1]==1){
        maxCount = max(maxCount,(count1+count2));
    }
 
    return maxCount;

}


int main(){
    vector<int> nums = {1,0,1,1,1,1,1,1,0,1,1,1,1,1};
    cout<<longestSubArray(nums);
}