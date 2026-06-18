from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {course: [] for course in range(numCourses)}

        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        visiting = set()
        visited = set()
        order = []

        def dfs(course: int) -> bool:

            if course in visiting:
                return False

            if course in visited:
                return True

            visiting.add(course)

            for prerequisite in graph[course]:
                if not dfs(prerequisite):
                    return False

            visiting.remove(course)

            visited.add(course)

            order.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return order