class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path=[]
        R,C=len(board),len(board[0])
        dirs=((1,0),(-1,0),(0,1),(0,-1))
        def bt(r,c):
            if len(path)==len(word):
                return True
            if not (0<=r<R and 0<=c<C) or board[r][c]=='#' or board[r][c]!=word[len(path)]:
                return False
            save=board[r][c]
            board[r][c]='#'
            path.append(save)
            for dr,dc in dirs:
                if bt(r+dr,c+dc):
                    return True
            board[r][c]=save
            path.pop()
            return False
        for r in range(R):
            for c in range(C):
                if bt(r,c):
                    return True
        return False
        
        