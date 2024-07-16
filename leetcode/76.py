class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_count = {}
        for c in t:
            if c not in char_count:
                char_count[c] = 0
            char_count[c] += 1

        char_indices = {}
        min_window = ""
        
        for i in range(len(s)):
            if s[i] in char_set:
                char_indices[s[i]] = i
                if char
                    start_char, start_index = min(char_indices.items(), key=lambda x: x[1])
                    end_index = max(char_indices.values())
                    
                    del char_indices[start_char]
                    print(s[start_index:end_index + 1])

        return s


sol = Solution()
print(sol.minWindow("ADOBECODEBANC", "ABC"))
