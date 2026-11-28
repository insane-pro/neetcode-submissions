class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        pos_dir=set()
        neg_dir=set()
        ret=[]
        cols=set()
        board=[['.']*n for _ in range(n)]
        def bt(r):
            if r==n:
                ret.append([''.join(row) for row in board])
                return
            for c in range(n):
                if c in cols or r+c in pos_dir or r-c in neg_dir:
                    continue
                board[r][c]='Q'
                cols.add(c)
                pos_dir.add(r+c)
                neg_dir.add(r-c)
                bt(r+1)
                neg_dir.remove(r - c)
                pos_dir.remove(r + c)
                cols.remove(c)
                board[r][c] = "."
        bt(0)
        return ret