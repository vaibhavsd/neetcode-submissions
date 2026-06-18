class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        myrowdict= dict()
        mycoldict= dict()
        mygriddict= dict()

        for i in range(9):
            for j in range(9):
                if not board[i][j]== '.':
                    if i in myrowdict:
                        if board[i][j] in myrowdict[i]:
                            return False
                        else:
                            myrowdict[i].append(board[i][j])
                    else:
                        myrowdict[i]= [board[i][j]]
                    if j in mycoldict:
                        if board[i][j] in mycoldict[j]:
                            return False
                        else:
                            mycoldict[j].append(board[i][j])
                    else:
                        mycoldict[j]= [board[i][j]]

                    if (int(i/3), int(j/3)) in mygriddict:
                        if board[i][j] in mygriddict[(int(i/3), int(j/3))]:
                            return False
                        else:
                            mygriddict[(int(i/3), int(j/3))].append(board[i][j])
                    else:
                        mygriddict[(int(i/3), int(j/3))]= [board[i][j]]

        print(myrowdict)
        print(mycoldict)
        print(mygriddict)

        return True