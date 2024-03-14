"""
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

"""
solution
Danh sách (List): toán tử in là tuyến tính O(n)

Tập hợp (Set) và từ điển (Dictionary):   O(1) (độ phức tạp trung bình), với điều kiện rằng phần tử đó không phải là một phần tử phức tạp như danh sách hoặc từ điển.
"""
from typing import List

def check_two_sum(arr : List[int],k : int) -> bool:
    arr_to_set = set(arr)
    for i in arr_to_set:
        if (k-i) in arr_to_set:
            return True
    return False

if __name__ == "__main__":
    print(check_two_sum([1,3,4],8))

"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
