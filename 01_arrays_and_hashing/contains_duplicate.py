"""
Contains Duplicate

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        countDict: dict = {}
        for num in nums:
            if countDict.get(num):   #if alr exists, ret True
                return True
            else:   #else include in hashmap
                countDict[num] = 1

        #if loop terminated, no dupes found
        return False



'''
hashmap put and get methods are O(1) expected time,
so for scanning through the list yields O(n)
'''

soln = Solution()
print(soln.hasDuplicate([1,2,3,4])) #False
print(soln.hasDuplicate([2,9,9,7,9])) #True


'''
MINIMALIST SOLUTION
```python
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)

CAVEAT
this does not have an early exit

```


ANOTHER METHOD WITH EARLY EXIT
```python
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num) #else add to set
        return False
```
'''
