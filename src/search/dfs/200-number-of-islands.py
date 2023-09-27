class Solution:
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]

    def dfs(self, grid, x, y):
        grid[x][y] = '0'
        for i in range(4):
            new_x = x + self.dx[i]
            new_y = y + self.dy[i]
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == '1':
                self.dfs(grid, new_x, new_y)

    def numIslands(self, grid: list[list[str]]) -> int:
        res = 0
        for x, row in enumerate(grid):
            for y, col in enumerate(row):
                if grid[x][y] == '1':
                    self.dfs(grid, x, y)
                    res += 1

        return res
