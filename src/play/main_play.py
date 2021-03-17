from train.train_utils import map_side_to_square, calc_squares_status
from train.train_utils import Board, Agent


def main(args):
    height, width = args.dims
    score1 = 0
    score2 = 0
    num_ties = 0
    win1 = 0
    win2 = 0
    for epoch in range(args.epochs):
        board = Board(height, width)
        agent1 = Agent(board, 0, True)
        agent2 = Agent(board, 0, False)
        i = 0
        while i < len(board.sides):
            i += 1
            print("turn: ", i)
            if agent1.turn:
                agent1.decide("randomly")
                if not agent1.turn:
                    agent2.set_turn(True)
            elif agent2.turn:
                agent2.decide("rule_based")
                if not agent2.turn:
                    agent1.set_turn(True)
            #print(f"agent1 score: {agent1.reward} {agent1.turn}")
            #print(f"agent2 score: {agent2.reward} {agent2.turn}")
            #input("press to continue...")
        if agent1.reward > agent2.reward:
            agent1.add_reward(100)
            win1 += 1
            #print("1 wins")
        elif agent1.reward < agent2.reward:
            agent2.add_reward(100)
            win2 += 1
            #print("2 wins")
        else:
            num_ties += 1
            # print("tie")
        score1 += agent1.reward
        score2 += agent2.reward
    print(score1, score2)
    print(f"1 wins {win1} times, 2 wins {win2} times, tie {num_ties} times")
