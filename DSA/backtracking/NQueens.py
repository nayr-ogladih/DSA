from tkinter import N


class NQueens:

    def __init__(self, n):
        self.n = n
        self.chess_table = [[0 for i in range(n)] for j in range(n)]

    # helper function
    def print_queens(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.chess_table[i][j] == 1:
                    print(" Q ", end='')
                else:
                    print(" - ", end='')
            print("\n")

    # helper function
    def is_placed_safe(self, row_index, col_index):
        #checks horizontally
        for i in range(self.n):
            if self.chess_table[row_index][i] == 1:
                return False

        # top left to right bottom
        j = col_index
        for i in range(row_index, -1, -1):
            if i < 0:
                break
            if self.chess_table[i][j] == 1:
                return False
            j -= 1

        # top right to bottom left
        for i in range(row_index, self.n):
            if i < 0:
                break
            if self.chess_table[i][j] == 1:
                return False
            j -= 1

        return True

    # declare new method
    def solve(self, col_index):
        if col_index == self.n:
            return True

        for row_index in range(self.n):
            if self.is_placed_safe(row_index, col_index):
                self.chess_table[row_index][col_index] = 1
                if self.solve(col_index + 1):
                    return True
                
                #backtracking
                self.chess_table[row_index][col_index] = 0

        return False

    def solve_NQueens(self):
        if self.solve(0):
            self.print_queens()
        else:
            print("There is no soultion for the problem!")






queens = NQueens(4)
queens.solve_NQueens()