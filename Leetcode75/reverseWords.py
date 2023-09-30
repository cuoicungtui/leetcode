def reverseWords(s):
    s = s.split()[::-1]
    # k = []
    # for i in s:
    #     k.insert(0,i)
    return ' '.join(s)
s = 'the sky is blue'
print(reverseWords(s))