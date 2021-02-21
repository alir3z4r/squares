from .train_utils import map_side_to_square, calc_squares_status 


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
        num_counts = calc_squares_status(squares)
        print(num_counts)

if __name__ == "__main__":
    i_side = int(input("Enter side index: "))
    cells = map_side_to_square(4,6,i_side)
    print(cells)
        
        
    
