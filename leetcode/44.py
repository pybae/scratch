class Solution:
    # let's try DFS with memoization
    def isMatch(self, s: str, p: str) -> bool:
        matches = {}
        return self.dfs(s, p, matches)

    def dfs(self, s: str, p: str, matches: dict):
        if s not in matches:
            matches[s] = {}
        
        if p in matches[s]:
            return matches[s][p]

        if s == "":
            if p == "" or p == "*":
                matches[s][p] = True
            elif p[0] == "*":
                matches[s][p] = self.dfs(s, p[1:], matches)
            else:
                matches[s][p] = False
        elif p == "":
            matches[s][p] = False
        else:
            if p[0] == "*":
                matches[s][p] = self.dfs(s[1:], p, matches) or self.dfs(s[1:], p[1:], matches) or self.dfs(s, p[1:], matches)
            elif p[0] == s[0] or p[0] == "?":
                matches[s][p] = self.dfs(s[1:], p[1:], matches)
            else:
                matches[s][p] = False

        return matches[s][p]

sol = Solution()
print(sol.isMatch("cb", "?a"))
