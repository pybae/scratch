import math

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        smallest, smallest_length = None, math.inf
        for s in strs:
            if len(s) < smallest_length:
                smallest = s
                smallest_length = len(s)

        i = 0
        while i < smallest_length:
            if all(s[i] == smallest[i] for s in strs):
                i += 1
            else:
                break 

        return smallest[0:i]

