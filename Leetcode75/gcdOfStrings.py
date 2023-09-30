str1 = "LEET"
str2 = "CODE"

while str1!=str2 and len(str1) != len(str2) :
    if len(str1)>len(str2):
        if str1[0:len(str2)] == str2:
            str1 = str1[len(str2):]
        else:
            break

    if len(str1)< len(str2):
        if str2[0:len(str1)] == str1:
            str2 = str2[len(str1):]
        else:
            break

# print(str1[0:len(str2)])
print(str1," ",str2)

    