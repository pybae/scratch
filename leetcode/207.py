from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # if no prereq is defined, we can assume we can take it.
        # so the question is whether there is a cycle in this graph
        # basically can we resolve all pre-requisites
        # [ai, bi], [1, 0], to take 1, you must have taken 0

        can_complete: dict[int, bool] = {}
        prereqs_for_course: dict[int, list[list[int]]] = {}

        for prereq in prerequisites:
            if prereq[0] not in prereqs_for_course:
                prereqs_for_course[prereq[0]] = []
            prereqs_for_course[prereq[0]].append(prereq[1])

        has_prereqs = set(prereq[0] for prereq in prerequisites)
        for i in range(numCourses):
            if i not in has_prereqs:
                can_complete[i] = True

        # attempt to resolve every prereq
        for course in has_prereqs:
            if not self.resolve_prereqs(course, prereqs_for_course, can_complete):
                return False

        return True

    def resolve_prereqs(self, course: int, 
                        prereqs_for_course: dict[int, list[list[int]]], 
                        can_complete: dict[int, bool]) -> bool:
        if course in can_complete:
            return can_complete[course]

        # use False as a visited flag
        can_complete[course] = False

        for required_course in prereqs_for_course[course]:
            if not self.resolve_prereqs(required_course, prereqs_for_course, can_complete):
                return False

        can_complete[course] = True
        return True

sol = Solution()
print(sol.canFinish(2, [[1, 0]]))
print(sol.canFinish(2, [[1, 0], [0, 1]]))
