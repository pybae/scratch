class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0

        while i < len(haystack):
            if haystack[i] == needle[0]:
                j = i + len(needle)
                if j <= len(haystack) and haystack[i:j] == needle:
                    return i
            i += 1

        return -1

sol = Solution()
print(sol.strStr("sadbutsad", "sad"))
print(sol.strStr("leetcode", "leeto"))
