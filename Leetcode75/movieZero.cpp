#include<iostream>
#include<vector>

using namespace std;

void moveZeroes(vector<int>& nums) {
    int start = 0;
    int end = 1;

    if (nums.size()<2) return;

    while(end != nums.size() ){
        
       if(nums[start] !=0){
            start+=1;
            end+=1;
       }else{
            if(nums[end] ==0){
                end+=1;
            }else{
                swap(nums[start],nums[end]);
                start+=1;
                end+=1;
            }
       }
    //    cout<<start<<" "<<end<<endl;

    }
};

int main(){
    vector<int> my_vector = {0};

    moveZeroes(my_vector);

    cout << "nnVector 1: "; 
    for (int i = 0; i < my_vector.size(); i++) 
        cout << my_vector[i] << " "; 
       
}