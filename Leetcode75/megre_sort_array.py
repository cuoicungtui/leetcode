# def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: None Do not return anything, modify nums1 in-place instead.
#         """
#         for i in range(m+n-1,0,-1):
#             print(i)
nums1 = [2,0]
m = 1
nums2 = [1]
n = 1
index1 = m-1
index2 = n-1

if (m==0):
   for i in range(0,n):
       nums1[i] = nums2[i]
else:
    for i in range(m+n-1,-1,-1):
        if index1 < 0 or index2 < 0:
            break
        if(nums1[index1] >= nums2[index2]):
            nums1[i] = nums1[index1]
            nums1[index1] = 0
            index1 -=1
        else:
            nums1[i] = nums2[index2]
            index2 -=1
    while index2>=0:
        nums1[index2] = nums2[index2]
        index2 -=1
print(nums1)
print(index1,index2)