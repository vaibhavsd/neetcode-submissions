class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            templist= []
            for j in range(9):
                if not board[i][j] == '.':
                    templist.append(board[i][j])
            if len(templist)!= len(set(templist)):
                print('False in rows')
                return False
                


        for i in range(9):
            templist= []
            for j in range(9):
                if not board[j][i] == '.':
                    templist.append(board[j][i])
            if len(templist)!= len(set(templist)):
                print('False in columns')
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                templist= []
                for k in range(3):
                    for l in range(3):
                        if not board[i+k][j+l]=='.' :
                            templist.append(board[i+k][j+l])
                if len(templist)!= len(set(templist)):
                    print('False in grids')
                    return False
        
        return True