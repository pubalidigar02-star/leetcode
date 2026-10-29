class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        visited = set()
        min_cost = 0
        min_dist = [float('inf')] * n
        min_dist[0] = 0

        for _ in range(n):
            curr = -1

            for i in range(n):
                if i not in visited and (
                    curr == -1 or min_dist[i] < min_dist[curr]
                ):
                    curr = i

            visited.add(curr)
            min_cost += min_dist[curr]

            x1, y1 = points[curr]

            for i in range(n):
                if i not in visited:
                    x2, y2 = points[i]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    min_dist[i] = min(min_dist[i], dist)

        return min_cost