import random
import copy


class Board(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.sides = (2*width*height + height + width)*[0]
        self.squares = [[4*[0] for _ in range(width)] for _ in range(height)]

    def map_square_to_side(coords):
        """
        Maps an element of square board to a side index
        """
        assert len(coords) == 3, "The coords must be of length 3"
        num_by_row_before = coords[0] * (2*self.width + 1)
        if coords[3] == 0:
            i_side = num_by_row_before + coords[2]
        elif coords[3] == 1:
            i_side = num_by_row_before + self.width + 1 + coords[2]
        elif coords[3] == 2:
            i_side = num_by_row_before + 2*self.width + 1 + coords[2]
        elif coords[3] == 3:
            i_side = num_by_row_before + self.width + coords[2]
        return i_side

    def map_side_to_square(self, i_side):
        """
        Maps the side index to squares
        """
        cells = []
        irow = i_side // (2*self.width + 1)
        i_row = irow if irow < self.height else self.height-1
        icol = i_side % (2*self.width + 1)
        i_col = icol if icol < self.width else min(
            icol-self.width, self.width-1)
        horizontal = True if icol < self.width else False
        if horizontal:
            if irow == 0 or irow == self.height:
                cells.append([i_row, i_col, 0 if irow == 0 else 2])
            else:
                cells.append([i_row, i_col, 0])
                cells.append([i_row-1, i_col, 2])
        else:
            if icol == self.width or icol == 2*self.width:
                cells.append([i_row, i_col, 3 if icol == self.width else 1])
            else:
                cells.append([i_row, i_col, 3])
                cells.append([i_row, i_col-1, 1])
        return cells

    def update(self, i_side, do_print=False):
        """
        Updates the board after adding a side
        """
        self.sides[i_side] = 1
        cells = self.map_side_to_square(i_side)
        for cell in cells:
            self.squares[cell[0]][cell[1]][cell[2]] = 1
        if do_print:
            self.print_out('both')
        return None

    def print_out(self, what='both'):
        """
        Prints out either sides or squares or both
        """
        if (what == 'sides' or what == 'both'):
            print(f"Sides list: {self.sides}")
        if (what == 'squares' or what == 'both'):
            print(f"Squares list: {self.squares}")
        return None

    def squares_stat(self, do_print=False):
        """
        Calculates how many squares with 0,1,2,3, or 4 sides are there in the
        square board
        """
        sums_list = [sum(x) for row in self.squares for x in row]
        sums_list_squares = [[sum(x), j, i] for j, row in enumerate(
            self.squares) for i, x in enumerate(row)]
        num_counts = [sums_list.count(i) for i in range(5)]
        if do_print:
            print(f"Squares statistics: {num_counts}")
        return num_counts, sums_list_squares


def squares_with_K_sides(squares, K):
    num_counts, sums_list = calc_squares_status(squares)
    K_squares = [sq[1:] for sq in sums_list if sq[0] == K]
    return K_squares


def empty_sides_Ksquares(squares, K):
    """
    Finds all the empty sides of a square with K filled sides

    Params:
        squares:    The squares list
        K:          The number of filled sides

    Returns:
        K_squares:  The squares coordinates with K filled sides
        empties:    indexes of empty sides in all of K_squares (the same size of K_squares)
        sides:      indexes of empty sides of K_squares in the entire board (same size)
    """
    height, width = len(squares), len(squares[0])
    K_squares = squares_with_K_sides(squares, K)
    empties = []
    sides = []
    for ks in K_squares:
        sq = squares[ks[0]][ks[1]]
        empties.append([i for i, s in enumerate(sq) if s == 0])
        sides += [map_square_to_side(height, width, [ks[0], ks[1], i])
                  for i, s in enumerate(sq) if s == 0]
    return K_squares, empties, sides


def map_square_to_side(height, width, coords):
    """
    Maps an element of square board to a side index
    """
    assert len(coords) == 3, "The coords must be of length 3"
    num_by_row_before = coords[0] * (2*width + 1)
    if coords[2] == 0:
        i_side = num_by_row_before + coords[1]
    elif coords[2] == 1:
        i_side = num_by_row_before + width + 1 + coords[1]
    elif coords[2] == 2:
        i_side = num_by_row_before + 2*width + 1 + coords[1]
    elif coords[2] == 3:
        i_side = num_by_row_before + width + coords[1]
    return i_side


def map_side_to_square(height, width, i_side):
    """
    Maps the side index to squares
    """
    cells = []
    irow = i_side // (2*width + 1)
    i_row = irow if irow < height else height-1
    icol = i_side % (2*width + 1)
    i_col = icol if icol < width else min(icol-width, width-1)
    horizontal = True if icol < width else False
    if horizontal:
        if irow == 0 or irow == height:
            cells.append([i_row, i_col, 0 if irow == 0 else 2])
        else:
            cells.append([i_row, i_col, 0])
            cells.append([i_row-1, i_col, 2])
    else:
        if icol == width or icol == 2*width:
            cells.append([i_row, i_col, 3 if icol == width else 1])
        else:
            cells.append([i_row, i_col, 3])
            cells.append([i_row, i_col-1, 1])
    return cells


def calc_squares_status(squares):
    """
    Calculates how many squares with 0,1,2,3, or 4 sides are there in the
    square board
    """
    sums_list = [sum(x) for row in squares for x in row]
    sums_list_squares = [[sum(x), j, i] for j, row in enumerate(
        squares) for i, x in enumerate(row)]
    num_counts = [sums_list.count(i) for i in range(5)]
    return num_counts, sums_list_squares


class Agent(object):
    def __init__(self, board, reward, starter):
        self.board = board
        self.reward = reward
        self.starter = starter
        self.turn = True if starter else False
        self.action = None

    def set_turn(self, is_turn):
        self.turn = is_turn

    def add_reward(self, reward):
        self.reward += reward

    def decide(self, how='randomly'):
        stats, _ = self.board.squares_stat()
        empty_sides = [i for i, s in enumerate(self.board.sides) if s == 0]
        print("empties: ", empty_sides)
        stats4_before = stats[-1]
        if how == 'randomly':
            selected_side = random.choice(empty_sides)
            self.board.update(selected_side)
            self.action = self.board.map_side_to_square(selected_side)
        elif how == "rule_based":
            print(stats)
            if stats[3] > 0:
                _, _, esides3 = empty_sides_Ksquares(self.board.squares, 3)
                print("3", esides3)
                selected_side = random.choice(esides3)
                self.action = self.board.map_side_to_square(selected_side)
                self.board.update(selected_side)
            elif (stats[0] > 0 or stats[1] > 0):
                _, _, esides0 = empty_sides_Ksquares(self.board.squares, 0)
                _, _, esides1 = empty_sides_Ksquares(self.board.squares, 1)
                esides01 = list(set(esides0).union(set(esides1)))
                print("01", esides01)
                lookfor = True
                
                while lookfor:
                    temp_board = copy.copy(self.board)
                    if len(esides01)>0:
                        selected_side = random.choice(esides01)
                        temp_board.update(selected_side)
                        new_stat, _ = temp_board.squares_stat()
                        print(self.board.squares == temp_board.squares)
                        if new_stat[3] == stats[3]:
                            lookfor = False
                            self.board.update(selected_side)
                        else:
                            esides01 = [s for s in esides01 if s != selected_side]
                    else:
                        print("22")
                        selected_side = random.choice(empty_sides)
                        self.board.update(selected_side)
                        self.action = self.board.map_side_to_square(selected_side)
                        lookfor = False

            else:
                print("2")
                selected_side = random.choice(empty_sides)
                self.board.update(selected_side)
                self.action = self.board.map_side_to_square(selected_side)
        stats, sums_list = self.board.squares_stat()
        if stats[-1] == stats4_before:
            self.turn = False
        else:
            self.reward += stats[-1]-stats4_before
        empty_sides = [i for i, s in enumerate(self.board.sides) if s == 0]
        print("empties after: ", empty_sides)

    def move(self):
        pass
