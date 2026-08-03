class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            seen=set()
            for j in range(9):
                if board[i][j]==".":
                    continue
                if board[i][j] in seen:
                    return False
                else:
                    seen.add(board[i][j])
        for i in range(9):
            sent=set()
            for j in range(9):
                if board[j][i]==".":
                    continue
                if board[j][i] in sent:
                    return False
                else:
                    sent.add(board[j][i])
        for row in range(0,9,3):
            for col in range(0,9,3):
                st=set()
                for i in range(row,row+3):
                    for j in range(col,col+3):
                        if board[i][j]==".":
                            continue
                        if board[i][j] in st:
                            return False
                        else:
                            st.add(board[i][j])
        for row in range(0,9,3):
            for col in range(0,9,3):
                st=set()
                for i in range(row,row+3):
                    for j in range(col,col+3):
                        if board[j][i] == ".":
                            continue
                        if board[j][i] in st:
                            return False
                        else:
                            st.add(board[j][i])
        return True
                
            