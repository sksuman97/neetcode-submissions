class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r_s, c_s, sq = defaultdict(set), defaultdict(set), defaultdict(set)
        r = 0

        for r in range(9):
            for c in range(9):
                if board[r][c]=='.':
                    continue
                if (board[r][c] in r_s[r]) or (board[r][c] in c_s[c]) or (board[r][c] in sq[(r//3,c//3)]):
                    return False
                r_s[r].add(board[r][c])
                c_s[c].add(board[r][c])
                sq[(r//3,c//3)].add(board[r][c])
        # print(sq)
        return True

