# def reverseVowels( s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         char_vowel='aeiouAEIOU'
#         list_vowel=[]
#         for i in range(len(s)):
#             if s[i] in char_vowel:
#                 list_vowel.insert(0,i)
#         if len(list_vowel)==1:
#              return s
#         s_spli = []
#         index = 0
#         for i in s:
#             if i in char_vowel:
#                 s_spli.append(s[list_vowel[index]]) 
#                 index+=1
#             else:
#                 s_spli.append(i)
#         return ''.join(s_spli)
# 

def reverseVowels(s):
    index_begin = 0
    index_end = len(s)-1
    char_vowel="aeiouAEIOU"
    if len(s)<2:
        return s
    # s = list(s)
    while index_begin < index_end:
        
        if s[index_begin] in char_vowel and s[index_end] in char_vowel:
            s[index_begin],s[index_end] = s[index_end] , s[index_begin]
            index_begin+=1
            index_end-=1

        if s[index_begin] not in char_vowel :
            index_begin+=1
        if s[index_end] not in char_vowel :
            index_end-=1
               
    return ''.join(s)
s = "Hello"
print(list(s))
print(reverseVowels(s))
