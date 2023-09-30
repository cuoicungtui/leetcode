def maxarea(height : list[int])-> int :

    """
    problem:
    Tim max area trong 1 list height
    area = min(height[i],height[j])*(j-i)
    input list height
    output max area

    solution problem:
    2 con trở left right
    left = 0
    right = len(height)-1
    area = 0
    left < right: i = i+1
    else j = j-1
    area = max(area,min(height[i],height[j])*(j-i))

    Gải thích:
    Duyệt qua mảng height vơi width giảm dần width = j-i
    Trực giác đằng sau điều này là nếu chúng ta giữ con trỏ tương ứng với chiều cao lớn hơn,
    thì có khả năng chúng ta có thể có diện tích lớn hơn.
    
    """
    
    left , right =  0 , len(height)-1
    print(left,right)
    area = 0
    while (left<right):
        area_new = (right - left) * min(height[left],height[right])
        area = max(area,area_new)

        if ( height[left]  < height[right] ):
            left+=1
        else:
            right-=1
    print(height[left], height[right],left,right)
    return area


height = [2,3,4,5,18,17,6]
print(maxarea(height))