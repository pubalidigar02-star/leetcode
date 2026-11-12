
class Solution:
    def dfs(self, isConnected, visited, city):
        visited[city] = True

        for i in range(len(isConnected)):
            if isConnected[city][i] == 1 and not visited[i]:
                self.dfs(isConnected, visited, i)

    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for i in range(n):
            if not visited[i]:
                provinces += 1
                self.dfs(isConnected, visited, i)

        return provinces
