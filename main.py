
sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
from prettytable import PrettyTable
import prettytable


class SudokuBox:
    def __init__(self, table:list,print_result:bool=False) -> None:
        self.table = table 
        if self.solve():
            print("Solved Sudoku:")
            self.print_board()
        else:
            print("No solution exists.")       

    def get_box(self, box_id:tuple):
        row, col = box_id
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        box = []
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                box.append(self.table[r][c])
        return box

    def find_empty(self):
        for row in range(9): # Selects a row
            for col in range(9): # Loops over the colums in the row
                if self.table[row][col] == 0: # Checks if the row is full
                    return (row, col)
        return None # Returns none if there is no empty cells

    def check_box(self, box_id:tuple, ans): # Tuple (row,column) -start at 0
        row, col = box_id
        self.value = self.table[row][col] # Intager- PROBLEM no assignment has appened
        self.row = self.table[row] # List of intagers
        self.col = [x[col] for x in self.table] # List of intagers - Gets the value in the col index in all rows in the table
        self.square = self.get_box(box_id) # List of intagers

        if ans in self.row:
            return False
        if ans in self.col:
            return False
        if ans in self.square:
            return False
        
        return True

    def solve(self):
        empty_cell = self.find_empty()
        if not empty_cell:
            return True # If sudoku is not full
        
        row, col = empty_cell

        for num in range(1,10):
            if self.check_box(empty_cell,num):
                self.table[row][col] = num
                if self.solve():
                    return True
                self.table[row][col] = 0

        return False




    def print_board(self):
        """Display the Sudoku board using PrettyTable."""
        table = PrettyTable(header=False, border=False.)

        for i, row in enumerate(self.table):
            # Replace zeros with dots for better readability
            formatted_row = [str(cell) if cell != 0 else '.' for cell in row]
            table.add_row(formatted_row)
        print(table)


# Initialize the solver with the given Sudoku puzzle
solver = SudokuBox(sudoku)
