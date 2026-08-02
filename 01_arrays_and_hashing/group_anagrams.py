"""
Group Anagrams

Time Complexity:  O()
Space Complexity: O()
"""

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups: dict = {} #{count tuple --> list[word]} mapping
        #key will alw be based on what im comparing against
        for word in strs:
            
            count: list[int] = [0] * 26 #increment each position based on word
            
            for char in word:
                position = ord(char) - ord('a')  #index like position
                count[position] += 1
            
            count = tuple(count)    #dict keys must be immutable
            if count not in groups:
                groups[count] = [word]
            else:
                groups[count].append(word)
        
        return list(groups.values())    #typecast default values view to a list

'''
===ALT MINIMALIST SOLUTION===
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)  #missing keys default to list() -> []
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            groups[tuple(count)].append(word)
        return list(groups.values())

'''
