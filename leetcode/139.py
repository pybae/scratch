from typing import Dict, List, Optional

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.remove_word(s, wordDict, 0, [None] * len(s))

    def remove_word(self, s: str, wordDict: List[str], index: int, cache: List[bool]) -> bool:
        if cache[index] is not None:
            return cache[index]

        for word in wordDict:
            if s[index:] == word:
                cache[index] = True
                return True
            if s[index:].startswith(word) and self.remove_word(s, wordDict, index + len(word), cache):
                return True

        cache[index] = False
        return False

sol = Solution()
print(sol.wordBreak("cars", ["ca", "rs"]))
print(sol.wordBreak("leetcode", ["leet", "code"]))
print(sol.wordBreak("applepenapple", ["apple", "pen"]))
print(sol.wordBreak("catsandog", ["cats", "dogs", "sand", "and", "cat"]))
print(sol.wordBreak("aaaaaaaaab", ["a", "aa", "aaa", "aaaa"]))
print(sol.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"]))
