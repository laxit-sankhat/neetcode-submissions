from typing import List


class Solution:
    def canFinish(
        self,
        numCourses: int,
        prerequisites: List[List[int]]
    ) -> bool:
        graph = {course: [] for course in range(numCourses)}

        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        visiting = set()

        def dfs(course: int) -> bool:
            if course in visiting:
                return False

            if not graph[course]:
                return True

            visiting.add(course)

            for prerequisite in graph[course]:
                if not dfs(prerequisite):
                    return False

            visiting.remove(course)

            graph[course] = []

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True