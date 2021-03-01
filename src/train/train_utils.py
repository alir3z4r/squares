import random


class Board:
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
        icol = i_side %  (2*self.width + 1)
        i_col = icol if icol<self.width else min(icol-self.width,self.width-1)
        horizontal = True if icol<self.width else False
        if horizontal:
            if irow == 0 or irow == self.height:
                cells.append([i_row,i_col,0 if irow == 0 else 2]) 
            else:
                cells.append([i_row,i_col,0])
                cells.append([i_row-1,i_col,2])
        else:
            if icol == self.width or icol == 2*self.width:
                cells.append([i_row,i_col,3 if icol==self.width else 1])
            else:
                cells.append([i_row,i_col,3])
                cells.append([i_row,i_col-1,1])
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
        sums_list_squares = [[sum(x),j,i] for j,row in enumerate(self.squares) for i,x in enumerate(row)]
        num_counts = [sums_list.count(i) for i in range(5)]
        if do_print:
            print(f"Squares statistics: {num_counts}")
        return num_counts, sums_list_squares


    



def map_square_to_side(height, width, coords):
    """
    Maps an element of square board to a side index 
    """
    assert len(coords) == 3, "The coords must be of length 3"
    num_by_row_before = coords[0] * (2*width + 1) 
    if coords[3] == 0:
        i_side = num_by_row_before + coords[2]
    elif coords[3] == 1:
        i_side = num_by_row_before + width + 1 + coords[2]
    elif coords[3] == 2:
        i_side = num_by_row_before + 2*width + 1 + coords[2]
    elif coords[3] == 3:
        i_side = num_by_row_before + width + coords[2]
    return i_side



def map_side_to_square(height, width, i_side):
    """
    Maps the side index to squares
    """
    cells = []
    irow = i_side // (2*width + 1) 
    i_row = irow if irow < height else height-1
    icol = i_side %  (2*width + 1)
    i_col = icol if icol<width else min(icol-width,width-1)
    horizontal = True if icol<width else False
    if horizontal:
        if irow == 0 or irow == height:
            cells.append([i_row,i_col,0 if irow == 0 else 2]) 
        else:
            cells.append([i_row,i_col,0])
            cells.append([i_row-1,i_col,2])
    else:
        if icol == width or icol == 2*width:
            cells.append([i_row,i_col,3 if icol==width else 1])
        else:
            cells.append([i_row,i_col,3])
            cells.append([i_row,i_col-1,1])   
    return cells


def calc_squares_status(squares):
    """
    Calculates how many squares with 0,1,2,3, or 4 sides are there in the 
    square board
    """
    sums_list = [sum(x) for row in squares for x in row]
    sums_list_squares = [[sum(x),j,i] for j,row in enumerate(squares) for i,x in enumerate(row)]
    num_counts = [sums_list.count(i) for i in range(5)]
    return num_counts, sums_list_squares


class Agent:
    def __init__(self, board, reward, starter):
        self.board = board
        self.reward = reward
        self.starter = starter
        self.turn = True if starter else False
   
    def set_turn(self, is_turn):
        self.turn = is_turn
       
    def decide(self, how='randomly'):
        stats, sums_list = self.board.squares_stat()
        empty_sides = [i for i,s in enumerate(self.board.sides) if s==0]      
        if how == 'randomly':
            stats4_before = stats[-1]
            selected_side = random.choice(empty_sides)
            self.board.update(selected_side)
            stats, sums_list = self.board.squares_stat()
            if stats[-1] == stats4_before:
                self.turn = False
            else:
                self.reward += stats[-1]-stats4_before

    def move(self):
        pass

