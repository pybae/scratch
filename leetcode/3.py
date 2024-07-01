class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        sub = set()
        left = 0
        for right in range(0, len(s)):
            while s[right] in sub:
                sub.remove(s[left])
                left += 1
            sub.add(s[right])
            ans = max(ans, len(sub))

        return ans


sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("bbbbbb"))
print(sol.lengthOfLongestSubstring("pwwkew"))
