word1 = "ab"
word2 = "pqrs"
out_str =''

index1 = 0
index2 = 0
while index1 < len(word1) or index2 < len(word2):
    if index1<len(word1) :
        out_str+=word1[index1]+' '
    if index2<len(word2) :
        out_str+=word2[index2]+' '
    index1+=1
    index2+=1
print(out_str)