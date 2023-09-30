def findMaxAverage(nums : list[int],k:int )-> float:
    start = 0
    end = start+k-1 
    sum_k = float(sum(nums[start:end+1]))
    
    maxAvg = sum_k/float(k)
    print(maxAvg)
    while(end < len(nums)-1):
        start += 1
        end +=1
        sum_k = float(sum_k+nums[end]- nums[start])
        avg =  sum_k/float(k)
        maxAvg = max(maxAvg,avg)
    print(start,end)
    return "{:.5f}".format(maxAvg)

nums = [1,12,-5,-6,50,3]
k = 3

print(findMaxAverage(nums,k))
