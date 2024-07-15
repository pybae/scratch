from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i = 0
        result = []

        while i < len(words):
            j, remainingWidth = i, maxWidth
            while j < len(words) and len(words[j]) <= remainingWidth:
                if len(words[j]) < remainingWidth:
                    remainingWidth -= 1
                remainingWidth -= len(words[j])
                j += 1
            

            if j == len(words): # i.e, last line
                result.append(self.leftJustify(words[i: j], maxWidth))
            else:
                result.append(self.evenlyJustify(words[i: j], maxWidth))
            i = j

        return result

    def evenlyJustify(self, words: List[str], maxWidth: int) -> str:
        extraSpaces = maxWidth - sum([len(word) for word in words])
        if len(words) == 1:
            return words[0] + extraSpaces * " "

        spaces_between_words = (extraSpaces // (len(words) - 1))
        remainder_spaces = extraSpaces % (len(words) - 1)
        print(extraSpaces, words)
        print(spaces_between_words, remainder_spaces)

        result = ""
        for i in range(0, len(words) - 1):
            num_spaces = spaces_between_words
            if remainder_spaces > 0:
                num_spaces += 1
                remainder_spaces -= 1
            result += words[i] + num_spaces * " "
        result += words[-1]
        return result

    def leftJustify(self, words: List[str], maxWidth: int) -> str:
        result = " ".join(words)
        result += (maxWidth - len(result)) * " "
        return result



sol = Solution()
# for word in sol.fullJustify(["This", "is", "an", "example", "of", "text",
#                              "justification."], 16):
#     print("[" + word + "]")
# 
# 
# for word in sol.fullJustify(["What","must","be","acknowledgment","shall","be"],
#                             16):
#     print("[" + word + "]")


for word in sol.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"],
                            20):
    print("[" + word + "]")
