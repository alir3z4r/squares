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
    num_counts = [sums_list.count(i) for i in range(5)]
    return num_counts


class Agent:
    def __init__(self, reward, starter):
        self.reward = reward
        self.starter = starter

    def move(self, squareBoard):


