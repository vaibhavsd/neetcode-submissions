class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            mset= set()
            for j in range(9):
                if board[i][j]!= '.':
                    if int(board[i][j]) in mset:
                        return False
                    else:
                        mset.add(int(board[i][j]))
        
        for j in range(9):
            mset= set()
            for i in range(9):
                if board[i][j]!= '.':
                    if int(board[i][j]) in mset:
                        return False
                    else:
                        mset.add(int(board[i][j]))

        for k in range(0,9,3):
            for m in range(0, 9, 3):
                mset= set()
                for i in range(3):
                    for j in range(3):
                        if board[i+k][j+m]!= '.':
                            if int(board[i+k][j+m]) in mset:
                                return False
                            else:
                                mset.add(int(board[i+k][j+m]))
        return True