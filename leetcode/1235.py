from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        We need to compute what the maximum profit is going to be at each endTime, so going from 0 -> max(endTime)
        For each endTime, find all jobs that end there, and use the prior array to key into it

        So start off with that map

        Okay, so we can't do DP because of memory constraints.
        What does this mean?

        Well, what we really need is just the dp of the start times to cache.
        i suppose you could memoize?
        or could you still just do the same thing but limit.

        i think you can do the same thing but limit right?
        and then the question is what about a start time that goes in between things?
        that's where you use binary search okay
        """

        jobs: list[tuple[int, int, int]] = list(zip(startTime, endTime, profit))
        jobs.sort(key=lambda x: x[1])

        # list of (end_time, profit) sorted by end_time
        profit_by_end_time: list[tuple[int, int]] = [(0, 0)]

        for job in jobs:
            start_time, end_time, profit = job

            i = self.find_profit_by_end_time(profit_by_end_time, end_time)
            j = self.find_profit_by_end_time(profit_by_end_time, start_time)

            profit = max(profit_by_end_time[i][1], profit_by_end_time[j][1] + profit)
            if profit_by_end_time[i][0] == end_time:
                profit_by_end_time[i] = (end_time, profit)
            else:
                profit_by_end_time.append((end_time, profit))

        return profit_by_end_time[-1][1]

    def find_profit_by_end_time(self, profit_by_end_time: list[tuple[int, int]], target: int) -> int:
        l, r = 0, len(profit_by_end_time)
        while l < r:
            mid = (l + r) // 2
            end_time, profit = profit_by_end_time[mid]

            if end_time == target:
                return mid
            elif end_time > target:
                r = mid
            else:
                l = mid + 1

        if l == 0:
            return 0
        return l - 1


sol = Solution()
print(sol.jobScheduling([1,2,3,3], [3,4,5,6], [50,10,40,70]))
print(sol.jobScheduling([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60]))
print(sol.jobScheduling([1,1,1], [2,3,4], [5,6,4]))
print(sol.jobScheduling(
    [4,3,1,2,4,8,3,3,3,9],
    [5,6,3,5,9,9,8,5,7,10],
    [9,9,5,12,10,11,10,4,14,7]
    ))
