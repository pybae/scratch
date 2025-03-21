from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        p_counts = Counter(p)
        s_counts = Counter(s[:len(p)])

        for i in range(len(p), len(s)):
            if s_counts == p_counts:
                result.append(i - len(p))

            s_counts[s[i - len(p)]] -= 1
            s_counts[s[i]] += 1
        
        if s_counts == p_counts:
            result.append(len(s) - len(p))
        return result


sol = Solution()
print(sol.findAnagrams("cbaebabacd", "abc"))
print(sol.findAnagrams("abab", "ab"))
print(sol.findAnagrams("ab", "ab"))

