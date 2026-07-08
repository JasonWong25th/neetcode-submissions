class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #assume all boards are guarentted to be 9 

        #First thought approch is to iterate over every single square
        #checking the value, compare that result with that row,
        #the column. and that 3 by 3 sub boxes.

        #some optimizations would be sets for each row, column
        #and sub box, as we iterate over each element
        #checking if it violates any rules

        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        sub_box_sets = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    box = (i // 3) * 3 + (j // 3)

                    if board[i][j] in row_sets[i] or board[i][j] in col_sets[j] or  board[i][j] in sub_box_sets[box]:
                        return False
                    row_sets[i].add(board[i][j])
                    col_sets[j].add(board[i][j])
                    sub_box_sets[box].add(board[i][j])
        return True