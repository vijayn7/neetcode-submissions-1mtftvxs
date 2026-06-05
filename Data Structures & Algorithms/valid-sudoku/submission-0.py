class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        s = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in s:
                    return False
                else:
                    s.add(board[i][j])
            
            s.clear()
        
        for j in range(9):
            for i in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in s:
                    return False
                else:
                    s.add(board[i][j])
            
            s.clear()

        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                for dx in range(3):
                    for dy in range(3):
                        if board[x + dx][y + dy] == '.':
                            continue
                        if board[x + dx][y + dy] in s:
                            return False
                        else:
                            s.add(board[x + dx][y + dy])
            
                s.clear()

        return True