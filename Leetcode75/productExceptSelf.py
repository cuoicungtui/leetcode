def productExceptSelf(nums: list[int]) -> list[int]:
    '''
    Cho một mảng số nguyên nums, 
    retur array answer sao cho answer[i] bằng tích của tất cả các phần tử của nums ngoại trừ nums[i] .
    O(n) thời gian và không sử dụng phép chia.

    Khởi tạo Mảng Left and Right  len = len(nums)

    arr_left[0] = 1
    arr_right[len-1] = 1

    arr_left[i] = arr_left[i-1]*num[i] 
    arr_right[i] = arr_right[i+1]+nums[len-1-i]

    Cach2 giảm memmory xuống với 1 for Time O(2n)

    tạo 1 mảng answer = [1 for _ in nums]

    cập nhât 2 đầu của mảng answer
    dung k1 k2 lưu tich của 2 đầu mảng

    '''
    answer = [1 for _ in nums]
    k1 = 1
    k2 = 1
    num_len = len(nums)
    for  i in range(1,num_len):
        k2 = k2*nums[i-1]
        answer[i] *= k2     
        k1*= nums[num_len-i]
        answer[num_len-i-1]*=k1 
    return answer

nums = [1,2,3,4]
print(productExceptSelf(nums))
        