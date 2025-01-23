class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        got = set()
        for j in range(len(grid[0])):
            count = 0
            t = []
            for i in range(len(grid)):
                if grid[i][j] == 1:
                    count += 1
                    t.append((i,j))
            if count > 1:
                for i in t:
                    got.add(i)
        for i in range(len(grid)):
            count = 0
            t = []
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count += 1
                    t.append((i,j))
            if count > 1:
                for i in t:
                    got.add(i)
        return len(got)
        