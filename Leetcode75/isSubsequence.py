def isSubsequence(s : str , t: str)->bool:

    """
    problem
    Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

    string t remove some char(can be none) -> s

    two poin

    check từng giá trị s trong t
    """
    if len(s)>len(t):
        return False
    if len(s)==0:
        return True
    index_s = 0 
    index_t = 0
    while index_t < len(t):
        if s[index_s] == t[index_t]: 
            index_s+=1
            if index_s >= len(s):
                return True
        index_t+=1
    return False
s = 'abc'
t = 'adsfsc'
print(isSubsequence(s,t))