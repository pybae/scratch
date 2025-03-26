from typing import List
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        result = 0
        work = Counter(tasks)
        cooldown = {}
        for task in work:
            cooldown[task] = 0

        while sum(work.values()) > 0:
            executable_tasks = set(task for task in cooldown if cooldown[task] <= 0)
            incomplete_tasks = [(task, work[task]) for task in work if task in executable_tasks and work[task] > 0]
            task_to_execute = max(incomplete_tasks, key=lambda x:x[1], default=None)

            if task_to_execute:
                work[task_to_execute[0]] -= 1
                cooldown[task_to_execute[0]] = n + 1

            for task in cooldown:
                cooldown[task] -= 1
            result += 1

        return result


sol = Solution()
print(sol.leastInterval(["A","A","A","B","B","B"], 2))
print(sol.leastInterval(["A","C","A","B","D","B"], 1))
print(sol.leastInterval(["A","A","A", "B","B","B"], 3))
print(sol.leastInterval(["B","C","D","A","A","A","A","G"], 1))
print(sol.leastInterval(["A","A","A","B","B","B","C","D","E","F","G","H","I","J","K"], 7))
