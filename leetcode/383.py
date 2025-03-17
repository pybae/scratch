from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = Counter(magazine)
        for c in ransomNote:
            if c not in counts or counts[c] == 0:
                return False
            counts[c] -= 1
        return True

sol = Solution()
print(sol.canConstruct("a", "b"))
print(sol.canConstruct("aa", "ab"))
print(sol.canConstruct("aa", "aab"))
