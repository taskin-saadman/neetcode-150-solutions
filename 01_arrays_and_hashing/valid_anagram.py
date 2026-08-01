"""
Valid Anagram

Time Complexity:  O(m+n), m and n are lengths of s and t
since we need 1 single pass through each of em
    Space Complexity: O(m+n) for the 2 count dictionaries
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       '''
       the count matters here, since we need to verify anagrams.
       so a dictionary is needed
       '''
       countDict1: dict = {}
       for char in s:
           if not countDict1.get(char):
               countDict1[char] = 1
           else:    #else just increment
               countDict1[char] = countDict1[char] + 1

       countDict2: dict = {}

       for char in t:
           if not countDict2.get(char):
               countDict2[char] = 1
           else:    #else just increment
               countDict2[char] = countDict2[char] + 1

       #finally, we will just compare the counts
       return countDict1 == countDict2



sol = Solution()
print(sol.isAnagram('racecar','carrace')) #True
print(sol.isAnagram('jar','jam'))  #False


'''
MINIMALIST VERSION
```python
    countDict1[char] = countDict1.get(char,0) + 1
```


ALT USING Counter module (outputs a dictionary of counts of each char)
```python
    from collections import Counter
    class Solution:
        def isAnagram(self, s, t)->bool:
            return Counter(s) == Counter(t)
```
'''
