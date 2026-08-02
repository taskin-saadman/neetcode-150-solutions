"""
Two Sum

the brute force solution would have used a nested loop
and compare sum of every element-pair to the target.
Although a correct solution, it would be O(n^2).

We will use dictionary to obtain O(n) solution.


Time Complexity:  O()
Space Complexity: O()
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen: dict = {} #num -> index mapping
        for idx, num in enumerate(nums):
            difference = target - num
            if difference in seen:
                return [seen[difference],idx]
            seen[num] = idx #else, update dict with idx value
            '''
            in hope of if in future difference potentially would exist in the dict
            ,save curr values idx into the dictionary
            COMPLEXITIES
            this is O(n) time and O(n) space
            dict get and put methods are O(1) expected time
            space is O(n) since in worst case target sum is not found
            '''

sol = Solution()
print(sol.twoSum([1,2,3,4,9], 11))
