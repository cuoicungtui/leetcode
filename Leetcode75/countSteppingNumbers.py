def cout_tree(start:int,end:int, max_num:int)-> int:
    if 


def countSteppingNumbers(low : str , hight : str) -> int:
    MOD = 10**9 + 7
    SUM = 0
    arr = [ i for i in range(len(low),len(hight)+1)]
    for i in range(1,len(arr)-1):
        # print(arr[i])
        SUM += (2**(arr[i]-1))*8 % MOD
        SUM%= MOD
        # SUM -=  ((2**(arr[i]-1))/2)% MOD
        # SUM%= MOD
    print(SUM)
    # Cần dưới Low - > 10**len(low)-1



countSteppingNumbers('98','1000')