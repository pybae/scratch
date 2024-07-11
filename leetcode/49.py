from typing import List, Dict
import json

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        frequencies = {}
        for s in strs:
            frequency = self.countFrequencies(s)
            if frequency not in frequencies:
                frequencies[frequency] = []
            frequencies[frequency].append(s)

        return list(frequencies.values())

    def countFrequencies(self, s: str) -> Dict[str, int]:
        result = {}
        for c in s:
            if c not in result:
                result[c] = 0
            result[c] += 1
        return ",".join(str(s) for s in sorted(result.items()))

sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(sol.groupAnagrams([""]))
print(sol.groupAnagrams(["a"]))


