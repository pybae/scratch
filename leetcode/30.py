from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []

        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1


        word_len = len(words[0])
        concat_word_len = len(words) * word_len
        for i in range(0, len(s) - concat_word_len + 1):
            current_word = s[i:i + concat_word_len]
            current_word_counts = {}
            for j in range(0, len(current_word), word_len):
                subword = current_word[j: j + word_len]
                if subword in word_counts:
                    current_word_counts[subword] = current_word_counts.get(subword, 0) + 1
                else:
                    break

            if word_counts == current_word_counts:
                result.append(i)

        return result

sol = Solution()
print(sol.findSubstring("barfoothefoobarman", ["foo", "bar"]))
print(sol.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))
print(sol.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))

