class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == '1':
                    count += 1

                    st = [[i, j]]

                    while st:
                        curr = st.pop()
                        grid[curr[0]][curr[1]] = '0'

                        for dx, dy in dirs:
                            if 0 <= curr[0] + dx < len(grid) and 0 <= curr[1] + dy < len(grid[0]) and grid[curr[0] + dx][curr[1] + dy] == '1':
                                st.append([curr[0] + dx, curr[1] + dy])

        return count