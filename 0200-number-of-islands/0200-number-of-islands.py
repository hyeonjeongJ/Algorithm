class Solution:
    def dfs(self, grid, i, j):
        if i <= -1 or j <= -1 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        # 한번 방문한 곳은 다시 방문하지 않도록 0으로 바꾸기
        
        grid[i][j] = '0'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)    
    
    def numIslands(self, grid):

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

   