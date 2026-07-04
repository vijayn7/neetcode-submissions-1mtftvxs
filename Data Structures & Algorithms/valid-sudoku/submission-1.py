class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        seen = set()

        # Check rows
        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if curr != '.':
                    if curr in seen:
                        return False
                    seen.add(curr)
            seen.clear()
        
        # Check columns
        for i in range(9):
            for j in range(9):
                curr = board[j][i]
                if curr != '.':
                    if curr in seen:
                        return False
                    seen.add(curr)
            seen.clear()

        dirs = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),  (0, 0),  (0, 1),
                (1, -1),  (1, 0),  (1, 1)]
        
        # Check 3x3 boxes
        for i in range(1, 9, 3):
            for j in range(1, 9, 3):
                seen.clear()

                for dx, dy in dirs:
                    curr = board[i + dx][j + dy]

                    if curr != '.':
                        if curr in seen:
                            return False
                        seen.add(curr)
        
        return True