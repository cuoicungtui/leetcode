def increasingTriplet(nums : list[int]) -> bool:
    '''
    Problem
    Input Array int 
    output Bool 
        True tồn tại bộ ba tăng dần không thay đổi vị trí
        False không tồn tại
    
    Yêu cầu : 
        Độ phức tạp O(n)  
        Độ phức tạp Không gian O(1)
    Hạn chế :
        1 <= nums.length <= 5 * 105
        -231 <= nums[i] <= 231 - 1

    Example :
    input :  nums =  arr[1,4,3,34,2]
    output:  True    (1,4,34)
    
    -----------------------------

    Problem solution

    two point 
        first and second 
    condition
        second > first 
    - Dùng 2 con trỏ lưu giá trị bé nhất thứ nhất và thứ 2
    - Số thứ nhất cập nhật khi gặp số bế hơn nó
    - Số thư 2 cập nhật khi gặp số lớn hơn số thư nhất và bé hơn số thứ 2
    - Dừng khi gặp số lớn hơn số thứ 1 và thứ 2 Trả về True
    - Kết thúc vòng lặp trả về False

    Example

    nums = [2,1,5,0,6]

    first = +OO   second = +OO
    step 1:  num = 2
    first = 2   second = +OO
    step 2: num = 1
    first = 1   second = +OO
    step 3: num = 5
    first = 1   second = 5
    step 4: num = 0 
    first = 0   second = 5
    step 5: num = 6
    first = 0   second = 5

    return True

    Cặp đầu ra 0 5 vì 6>0 nên hiên nhiên lớn hơn tât cả các số nó bé hơn ở vị trí trước nó.
    First(lấy ra số bé nhất trong vùng xét đại diện các số )
    
    Khi tồn tạo 1 second đồng nghĩa sẽ có các số thuộc first  
    Khi cập nhật second đồng nghĩa số đó thỏa mã lớn hơn first
    với điệu kiên bé hơn second_old -> chuyên qua bước đẹp mới-> second ko cần lớn hơn Các first cũ chi cần lớn hơn first hiện tại


    '''

    first =  second = float('inf')

    for num in nums:
        if  num <= first:
            first = num
        elif num<= second:
            second = num
        else:
            return True
    
    return False

nums = [5,4,3,2,1]
print(increasingTriplet(nums))