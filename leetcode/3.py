class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        substring = ""
        for i, c in enumerate(s):
            if c not in substring:
                substring += c
            else:
                substring = substring[substring.index(c) + 1:] + c
            result = max(result, len(substring))
        return result


sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("bbbbb"))
print(sol.lengthOfLongestSubstring("pwwkew"))
