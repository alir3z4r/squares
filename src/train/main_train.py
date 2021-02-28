from .train_utils import map_side_to_square, calc_squares_status 
from .train_utils import Board, Agent


def main(args):
    height, width = args.dims
    board = Board(height, width)
    agent1 = Agent(board,0,True)
    agent2 = Agent(board,0,False)
    i = 0
    while i<len(board.sides):
        """
        i_side = int(input("Enter side index: "))            
        if i_side<len(board.sides) and board.sides[i_side]==0:
            board.update(i_side)
            i += 1
        elif i_side>=len(board.sides):
            print("invalid")
        else: 
            print(f"side {i_side} has been already selected")
        
        board.update(i_side)
        board.print_out()
        counts = board.squares_stat(True)
        num_counts, sums_list = calc_squares_status(board.squares)
        print(f"sum list: {sums_list}")

        agent.decide()
        """
        i += 1
        print("turn: ",i)
        if agent1.turn:
            agent1.decide()
        elif agent2.turn:
            agent2.decide()
        if not agent1.turn:
            agent2.set_turn(True)
        if not agent2.turn:
            agent1.set_turn(True)
        print("board: ", board.sides, board.squares)
        print("scores: ", agent1.reward, agent2.reward)
        
        