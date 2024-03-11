def embolden(s: str,lst: []) -> str:
    arr_check = [0 for i in range(len(s))]
    def tick (sub : str , start : int):
        for i in range(len(sub)):
            arr_check[start+i] = 1 
    def insert_tag(array_check : [],s : str) -> str:
        check = False
        result = ''
        tag_start = '<b>'
        tag_end = '</b>'
        for i in range(len(s)):
            # print("check inseart : " , result)
            if arr_check[i] == 0 and not check:
                result+=s[i]
                continue

            if arr_check[i] == 1 and check:
                result+=s[i]
                continue

            if arr_check[i] == 1 and not check:
                result+=tag_start
                result+=s[i]
                check = True
                continue

            if arr_check[i] ==0  and check:
                result+=tag_end  
                result+=s[i]                           
                check = False
                continue
        if arr_check[-1] == 1:
           result+=tag_end
        return result

    for sub in lst:
        start_find = s.find(sub)
        while start_find >= 0 :
            tick(sub,start_find)
            start_find = s.find(sub,start_find+1, len(s))

    return insert_tag(arr_check,s)

s = 'aaaaaaa'
lst = ['aaa','a','aaaa']

print(embolden(s,lst))