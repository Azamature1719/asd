class Queen:
    def __init__(self, _row, _column):
        self.row = _row
        self.column = _column
    
    def __str__(self):
        return f"{self.row} {self.column}"


class Board:
    FREE = 0
    FILLED = 1

    def __init__(self, _size):
        self.size = _size
        self.field = [[self.FREE] * _size for _ in range(_size)]

    def queen_here(self, queen):
        return self.field[queen.row][queen.column] == self.FILLED

    def fill_place(self, _id_row, _id_column):
        self.field[_id_row][_id_column] = self.FILLED

    def set_free(self, _id_row, _id_column):
        self.field[_id_row][_id_column] = self.FREE

    def under_attack(self, queen):
        # checking vertically and horizontally
        for field_pos in range(self.size):
            if self.queen_here(Queen(queen.row, field_pos)) or self.queen_here(Queen(field_pos, queen.column)):
                return True

        # checking diagonally
        for field_row in range(self.size):
            for field_column in range(self.size):
                if (field_row + field_column == queen.row + queen.column) or (field_row - field_column == queen.row - queen.column):
                    if self.queen_here(Queen(field_row, field_column)):
                        return True
        return False
    
    def place_queens(self, _size):
        if _size == 0:
            return True
        for row in range(self.size):
            for column in range(self.size):
                if (not self.under_attack(Queen(row, column))) and (self.field[row][column] != 1):
                    self.fill_place(row, column)
                    if self.place_queens(_size - 1) == True:
                        return True
                    self.set_free(row, column)
        return False
        
    def place_N_queens(self):
        self.place_queens(self.size)

    # print chess field
    def print(self):
        for row in self.field:
            print(row)


def main():
    print("Enter quantity of queens: ")
    board = Board(int(input()))
    board.place_N_queens()
    board.print()
    print("Size of the board == Number of queens")


if __name__ == "__main__":
    main()