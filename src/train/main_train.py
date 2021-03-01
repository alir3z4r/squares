from .train_utils import map_side_to_square, calc_squares_status 
from .train_utils import Board, Agent


def main(args):
    height, width = args.dims
    board = Board(height, width)
    agent1 = Agent(board,0,True)
    agent2 = Agent(board,0,False)
    i = 0
    while i<len(board.sides):
        i += 1
        print("turn: ",i)
        if agent1.turn:
            agent1.decide()
            if not agent1.turn:
                agent2.set_turn(True)
        elif agent2.turn:
            agent2.decide()
            if not agent2.turn:
                agent1.set_turn(True)
        print(f"agent1 score: {agent1.reward} {agent1.turn}")
        print(f"agent2 score: {agent2.reward} {agent2.turn}")
        input("press to continue...")
        
        