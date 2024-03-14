"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

"""
solution
[1,2,3,4,5]

()*(2,3,4,5) | (1)(3,4,5) | (1,2)(4,5) | (1,2,3)(5) | (1,2,3,4)()

"""
from typing import List

def withoutdivision(arr : List[int]) -> List[int]:
    L = [1 for i in range (len(arr)+1)]
    R = [1 for i in range (len(arr)+1)]
    result = [1 for i in range (len(arr))]
    L_index = 0
    R_index = len(arr)-1
    for i in range(len(arr)):
        L[L_index+1] = L[L_index] * arr[i]
        L_index+=1
        R[R_index-1] = R[R_index] * arr[len(arr)-i-1]
        R_index -=1
    for i in range(len(result)):
        result[i] = L[i]*R[i] 

    return result

if __name__ == "__main__":
    print(withoutdivision([1,2,3,4,5]))
    print(withoutdivision([1,1,3,1,1]))
