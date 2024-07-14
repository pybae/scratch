import math
from typing import List

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        digits = [str(i) for i in range(1, n + 1)]
        return self.recurse(n, k, digits)

    def recurse(self, n: int, k: int, digits: List[str]) -> str:
        if k == 1:
            return "".join(digits)

        i = len(digits) - n
        n_fact = math.factorial(n - 1)
        bucket = (k - 1) // n_fact
        digits[i], digits[i + bucket] = digits[i + bucket], digits[i]
        digits[i + 1:] = sorted(digits[i + 1:])

        remainder = k % n_fact
        if remainder == 0:
            remainder = n_fact

        return self.recurse(n - 1, remainder, digits)


sol = Solution()
print(sol.getPermutation(3, 3))

"""
123
132
213
231
312

1234
1243
1324
1342
1423
1432
2134
2143
2314

so for 4 and 9
we know 3! = 6, and 9 // 6 = 1
so what, we choose 2


2, now we have three left

yeah gotta keep that state, sortedj
out of 1,3,4

3! = 2, 3 // 2 = 1
3 -> 1, 4
and we have onee left

2314 = 1, first to take

something like that?
hrm i think so?

6 means go in too, got it
3, 3

2! = 2, 3 - 2 = 1
so choose 
2, 

13, 1! = 1, 1 = 1
no-op since 1
if 1 always just return n
but always sort before recursing?
yeah it is a set.

more coding than math actually
"""
