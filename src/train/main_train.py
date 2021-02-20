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


def main(args):
    height, width = args.dims
    sides = (2*width*height + height + width)*[0] 
    print(sides)
    squares = [[4*[0] for _ in range(width)] for _ in range(height)]
    i = 0
    while i < len(sides):
        i_side = int(input("Enter side index: "))            
        if i_side<len(sides) and sides[i_side]==0:
            sides[i_side] = 1
            i += 1
        elif i_side>=len(sides):
            print("invalid")
        else: 
            print(f"side {i_side} has been already selected")            
        print(sides)
        filled_cells = map_side_to_square(height, width, i_side)
        print(squares)
        for cell in filled_cells:
            squares[cell[0]][cell[1]][cell[2]] = 1
        print(squares)

if __name__ == "__main__":
    i_side = int(input("Enter side index: "))
    cells = map_side_to_square(4,6,i_side)
    print(cells)
        
        
    
