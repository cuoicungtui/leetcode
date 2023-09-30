nums = [2,2,2]
val = 3
index = len(nums)-1
count = 0
i=0
while i < len(nums)-1:
    if nums[i] == val:
        nums[i] = nums[index]
        nums[index] = 10000
        index-=1
        i-=1
    i+=1
    if nums[i] == 10000:
        break
print(nums,i)