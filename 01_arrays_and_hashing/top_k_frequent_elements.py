"""
Top K Frequent Elements

Time Complexity:  O(n)
Space Complexity: O(n)
"""
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
       #count freq of each unique number
       counts: dict[int,int] = defaultdict(int)  #num-->count mapping
       for num in nums:
           counts[num] += 1 #new keys will have value 0

       #build buckets indexed by frequency
       #max possible freq is len(nums), so create n+1 buckets
       buckets =[[] for _ in range(len(nums) + 1)] #use list comprehension for empty buckets
       for num, freq in counts.items():
           '''
           Here, we iterate over counts.items(), which has u entries (at worst case u is n),
           and each append is amortized O(1). That is O(u) ≤ O(n).
           '''
           #append since each bucket itself is also a list
           buckets[freq].append(num)

       #collect results from highest frequency down
       result = []
       #in worst case, we touch O(u+n) numbers in total ~ O(n)
       for bucket in reversed(buckets): #nth bucket means freq = n 
           for num in bucket:
               result.append(num)
               if len(result) == k:
                   return result
       return result  #topk elements was not found          

soln = Solution()
print(soln.topKFrequent([1,2,2,3,3,3], 2))

'''
MINIMALIST SOLUTION USING COUNTER
```pytyhon
from collections import Counter

class Solution:
        def topKFrequent(self, nums, k) -> list[int]:
            buckets = [[] for _ in range(len(nums) + 1)]
            for num, freq in Counter(nums).items():
                buckets[freq].append(num)
            #nested list comprehension
            return [num for bucket in reversed(buckets) for num in bucket][:k]
```
'''
