from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edge_map = defaultdict(list)
        in_degree = [0] * numCourses
        for next, pre in prerequisites:
            in_degree[next] += 1
            edge_map[pre].append(next)
        queue = [node for node in range(numCourses) if in_degree[node] == 0]
        while queue:
            node = queue.pop(0)
            for next_node in edge_map[node]:
                in_degree[next_node] -= 1
                if in_degree[next_node] == 0:
                    queue.append(next_node)
        return sum(in_degree) == 0

        




print(Solution().canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))