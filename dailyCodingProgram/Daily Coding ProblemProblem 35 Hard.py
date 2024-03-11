# Daily Coding Problem: Problem #35 [Hard]
# two point
arr = ['G','R','B','G','R','R','B','R','G']
#arr = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
l=0
r=len(arr)-1
dem=0
while l<r:
    if arr[l]=="R":
        l=l+1
        dem=dem+1
    if arr[l]=="B" or arr[l]=="G":
        swapValue = arr[l]
        arr[l] =  arr[r]
        arr[r] = swapValue
        r=r-1
  
l = dem+1
r=len(arr)-1

while l<r:
    if arr[l]=="G":
        l=l+1       
    if arr[l]=="B":
        swapValue = arr[l]
        arr[l] =  arr[r]
        arr[r] = swapValue
        r=r-1
print(arr)
