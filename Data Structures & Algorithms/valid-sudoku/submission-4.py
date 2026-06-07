class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for lis in board:
            current = []
            for i in lis:
                if i.isnumeric():
                    current.append(i)
            has_duplicates = len(current) != len(set(current))
            if has_duplicates:
                return False

        for j in range(9):
            col = []
            for i in range(9):
                if board[i][j].isnumeric():
                    col.append(board[i][j])
            has_duplicates = len(col) != len(set(col))
            if has_duplicates:
                return False

            
        box = []
        for row in range(3):
            for col in range(3):
                box= []
                for i in range(3):
                    for j in range(3):
                        if board[row*3+i][col*3+j].isnumeric():
                            box.append(board[row*3+i][col*3+j])
                has_duplicates = len(box) != len(set(box))
                if has_duplicates:
                    return False
        else:
            return True



            

                    
                
                
            
