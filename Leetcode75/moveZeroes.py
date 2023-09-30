def moveZeroes(nums : list[int]) -> None:
    """
        Problem
        Input array[int]
        move all 0 to back list while maintaining the relative order of the non-zero elements.

        example
        input : nums = [1,4,0,0,12,45,3,0]
        output : nums = [1,4,12,45,3,0,0,0]

        Problem solution

        Create Zoro Queue
            enqueue position Zero New
            dequeue position Zero old
        index = 0 count position Zero

        index = 0  Not update position Num with Num != 0

        if Num != 0 and index>0 
            swap (position Num, dequeue position zero  )
            update zero queue position Zero new = position num

        k = count(zero)
        memmory O(n+k) -> Max memmory O(2n) k = n

        Time  O(2n)
    """
    from collections import deque

    zero_queue = deque()
    for i, num in enumerate(nums):
        if num !=0 and len(zero_queue) >0:
            # pos_zero = zero_queue.popleft()
            nums[zero_queue.popleft()] = num
            nums[i] = 0
            zero_queue.append(i)
            continue
        if num == 0:
            zero_queue.append(i)
    # print(nums)
        

def moveZeroes2( nums: list[int]) -> None:
    """
    dụng ý tưởng nổi bọt liên tục cạp nhật các vị trí bằng 0 ơ trước
    """

    l=0
    for r in range(len(nums)):
        if nums[l]==0 and nums[r]!=0:
            tmp=nums[l]
            nums[l]=nums[r]
            nums[r]=tmp
            l+=1

        # if nums[l] !=0:
        #     l+=1
    print(nums)

NUMS = [0,1,0,3,12]
moveZeroes2(NUMS)



