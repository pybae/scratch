from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        I think this can be done greedily?

        so start off at 0, iterate until you find a match,
        if you find no match, return "", finding match is done by Counter, doing some thing, it's 26 character comparison so quick enough.

        or just decrement and sum counts, same thing. maybe comparison is faster actually? let's try that.

        and then what happens if you fail...
        means you should iterate to the next character that is in t, subtract the one you're currently in,
        then try expand again, from the end of that.?

        so two pointers, and Counter
        """

        result = None
        t_counts = Counter(t)
        start, end = 0, 0 

        while start < len(s) and s[start] not in t_counts:
            start += 1

        if start < len(s):
            t_counts[s[start]] -= 1
        end = start + 1

        while end <= len(s):
            if all(x <= 0 for x in t_counts.values()):
                if not result:
                    result = s[start:end]
                result = s[start:end] if end - start - 1 < len(result) else result

                t_counts[s[start]] += 1
                start += 1
                while start < len(s) and s[start] not in t_counts:
                    start += 1
            elif end < len(s) and s[end] in t_counts:
                t_counts[s[end]] -= 1
                end += 1
            else:
                end += 1


        return result if result else ""

sol = Solution()
# print(sol.minWindow("ADOBECODEBANC", "ABC"))
# print(sol.minWindow("a", "a"))
# print(sol.minWindow("a", "aa"))
# print(sol.minWindow("ab", "a"))
# print(sol.minWindow("ab", "b"))
# print(sol.minWindow("a", "b"))
print(sol.minWindow("acbbaca", "aba"))
