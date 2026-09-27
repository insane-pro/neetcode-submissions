class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen=set()
            for i in range(9):
                v=board[row][i]
                if v==".":
                    continue
                if v in seen:
                    return False
                seen.add(v)
        for col in range(9):
            seen=set()
            for i in range(9):
                v=board[i][col]
                if v==".":
                    continue
                if v in seen:
                    return False
                seen.add(v)
        for bi in (0, 3, 6):
            for bj in (0, 3, 6):
                seen = set()
                for n in range(3):
                    for m in range(3):
                        v = board[bi + n][bj + m]
                        if v == '.':
                            continue
                        if v in seen:
                            return False
                        seen.add(v)
        return True

        