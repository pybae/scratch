class Solution:
    def partitionString(self, s: str) -> int:
        partitions = 0
        char_map = {}

        for i in range(len(s)):
            if s[i] in char_map:
                partitions += 1
                char_map = {}
            char_map[s[i]] = i

        print(char_map)
        return partitions + 1


sol = Solution()
print(sol.partitionString("abacaba"))
print(sol.partitionString("ssssss"))
print(sol.partitionString("shkqbyutdvknyrpjof"))
