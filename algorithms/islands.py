class Solution():
    def adjacent_list_representation(self, grid):
        rep = dict()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                coord = (x, y)
                edges = self.get_edges(x, y, grid)
                if len(edges) != 0:
                    rep[coord] = edges
        return rep

    def get_edges(self, i, j, grid):
        if int(grid[i][j]) == 0:
            return list()

        # up, down, left, right
        up = (i - 1, j)
        down = (i + 1, j)
        left = (i, j - 1)
        right = (i, j + 1)
        edges = list()
        for direction in [up, down, left, right]:
            i, j = direction[0], direction[1]
            max_i, max_j = len(grid), len(grid[0])
            try:
                # if i == -1 or j == -1:
                #     continue
                # if i > max_i or j > max_j:
                #     continue
                if int(grid[i][j]) == 0:
                    continue
                edge = grid[i][j]
                edges.append((i, j))
            except:
                continue
        return edges

    def BFS(self, graph):
        visited, fringe = set(), list()
        num_islands = 0
        for vertex, edges in graph.items():
            if vertex in visited:
                continue
            if not self.not_adjacent(vertex[0], vertex[1], visited, graph):
                num_islands += 1
            visited.add(vertex)
            for e in edges:
                fringe.append(e)

            while (len(fringe) != 0):
                # print vertex, fringe
                edge = fringe.pop(0)
                print edge
                for e in graph[edge]:
                    if e not in visited:
                        fringe.append(e)
                visited.add(e)
        return num_islands

    def not_adjacent(self, i, j, visited, graph):
        if len(visited) == 0:
            return True
        last_added = list(visited)[-1]
        diffx, diffy = abs(last_added[0] - i), abs(last_added[1] - j)
        if diffx > 1 or diffy > 1:
            return False
        else:
            return True

    def numIslands(self, grid):
        graph = self.adjacent_list_representation(grid)
        return self.BFS(graph)


s = Solution()
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print s.numIslands(grid)

