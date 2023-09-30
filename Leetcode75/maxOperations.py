def maxOperations(nums : list[int] , k : int ) -> int:
    '''
    Input list int  and number k
    in số lượng các cặp có tông bằng k trong list 

    '''
    list_num = []
    for i in nums:
        if  i< k :
            list_num.append(i)
    list_num = sorted(list_num)

    left, right = 0,len(list_num)-1
    count = 0
    while left < right:
        if list_num[left] + list_num[right] == k :
            left +=1
            right-=1
            count+=1
        elif list_num[right] > (k - list_num[left]):
            right-=1
        else:
            left+=1

    return count


nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
k = 2
print(maxOperations(nums,k))