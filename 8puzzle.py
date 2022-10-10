import math


class puzzle_8:
    Size = 3

    initial_state = [
        [1, 8, 2],
        [0, 4, 3],
        [7, 6, 5]
    ]

    final_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    depth = 0

    def valid_coordinates(self, coords:list[int]):
        row = coords[0]
        col = coords[1]

        return row > -1 and row < self.Size and col > -1 and col < self.Size

    def possible_moves(self, coords: list[int]):
        moves = []

        row, col = coords[0], coords[1]

        # move up
        _row, _col = row - 1, col

        if self.valid_coordinates([_row, _col]):
            moves.append([_row, _col])

        # move left
        _row, _col = row, col - 1

        if self.valid_coordinates([_row, _col]):
            moves.append([_row, _col])

        # move right
        _row, _col = row, col + 1

        if self.valid_coordinates([_row, _col]):
            moves.append([_row, _col])

        # move down
        _row, _col = row + 1, col

        if self.valid_coordinates([_row, _col]):
            moves.append([_row, _col])

        return moves

    def find_position(self, n, state):
        i, j = 0, 0

        for row in state:
            j = 0
            for num in row:
                if num == n:
                    return [i, j]
                j += 1
            i += 1

        return [-1, -1]

    def puzzle_move(self, puzzle, move):
        coords = self.find_position(0, puzzle)

        row, col = move[0], move[1]
        _row, _col = coords[0], coords[1]

        # swap
        puzzle[_row][_col], puzzle[row][col] = puzzle[row][col], puzzle[_row][_col]

        return puzzle

    def back_to_previous_state(self, puzzle, coords):
        move = self.find_position(0, puzzle)

        row, col = move[0], move[1]
        _row, _col = coords[0], coords[1]

        # swap
        puzzle[_row][_col], puzzle[row][col] = puzzle[row][col], puzzle[_row][_col]

        return puzzle

    def solve(self, puzzle: "list[int][int]" = initial_state):

        if self.final_state == puzzle:
            self.print_puzzle(puzzle)
            return

        coords = self.find_position(0, puzzle)
        moves = self.possible_moves(coords)
        print(moves)
        manhattan = math.inf

        best_move = [-1, -1]

        for move in moves:
            puzzle = self.puzzle_move(puzzle, move)
            h = self.manhattan_distance(puzzle)

            if h < manhattan:
                manhattan = h
                best_move = move

            puzzle = self.back_to_previous_state(puzzle, coords)

        puzzle = self.puzzle_move(puzzle, best_move)

        self.depth += 1
        self.print_puzzle(puzzle)
        self.solve(puzzle)

        return moves

    def manhattan_distance(self, puzzle):
        distance = 0

        for row in puzzle:
            for n in row:
                if n == 0:
                    continue

                d = 0

                pos_initial = self.find_position(n, puzzle)
                pos_final = self.find_position(n, self.final_state)

                d += abs(pos_initial[0] - pos_final[0])
                d += abs(pos_initial[1] - pos_final[1])

                distance += d

        return distance

    def print_puzzle(self, puzzle):
        for row in puzzle:
            for num in row:
                print(num, end=" ")
            print()

        print()


puzzle__ = puzzle_8()
puzzle__.solve()
print("No of moves required to get final state: ", puzzle__.depth)