class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ## TO verify each row doesn't have duplicates
        for r in range(9):
            unique = set()
            for c in range(9):
                if board[r][c] =='.':
                    continue
                if board[r][c] in unique:
                    return False
                unique.add(board[r][c])
        ## To verify each column doesn't have duplicates
        for c in range(9):
            unique = set()
            for r in range(9):
                if board[r][c] =='.':
                    continue
                if board[r][c] in unique:
                    return False
                
                unique.add(board[r][c])
        ## To verify each 3*3 block doesn't have duplicates
        r_s = 0
        while r_s<9:
            c_s=0
            while c_s<9:
                unique = set()
                for r in range(3):
                    for c in range(3):
                        if board[r_s+r][c_s+c] =='.':
                            continue
                        if board[r_s+r][c_s+c] in unique:
                            return False
                        unique.add(board[r_s+r][c_s+c])
                c_s+=3
            r_s+=3
        return True
                



