#1497: Check if Arrays Pair are divisible by K
'''Given an array of integers arr of even length n and an integer k.

We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

Return true If you can find a way to do that or false otherwise.'''

'''Example 1:

Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
Output: true
Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).'''
from collections import Counter

class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        # Count the frequency of each remainder when each element in arr is divided by k
        remainder_count = Counter(x % k for x in arr)
    
        # Check if the number of elements that are divisible by k is even
        if remainder_count[0] % 2 != 0:
            return False
    
        # Check if each non-zero remainder has a complementary count of elements
        # Such that remainder + complementary = k
        # The counts of remainder and its complementary need to be the same
        for remainder in range(1, k):
            if remainder_count[remainder] != remainder_count[k - remainder]:
                return False
            
        # All checks have passed, hence return True
        return True
