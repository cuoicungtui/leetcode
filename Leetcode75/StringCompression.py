def compress(chars: list[str]) -> int:

    '''
    Problem
    Nén mảnh kí tự băng cách đếm các kí tự đó 
    đưa ra tổng số kí tự dùng để nén

    input : chars : List[str]
    output: int (Tổng số kí tự dùng để nén)

    Problem solution

    Two point 
    frist - end lưu vị trí đầu cuối của các kí tự được lặp lại
    val_char lưu lại kí tự đang xét
    char khác end cập nhật frist = end

    return index   index = quantity (position chars update)

    '''
    frist = 0
    end = -1
    val_char = chars[0]
    index = 0
    for i, char in enumerate(chars):
        if char != val_char:
            chars[index] = val_char
            index+=1
            if end != frist:
                for j in str(end-frist+1):
                     chars[index] = j
                     index+=1
            frist = end = i
            val_char = char
        else:
            end+=1

    chars[index] = val_char
    index+=1
    if end != frist:
        for j in str(end-frist+1):
                chars[index] = j
                index+=1
    # print(chars)
    return index

chars = ["a","a","b","b","c","c","c"]
print(compress(chars))
