from .train_utils import map_side_to_square, calc_squares_status
from .train_utils import Board, Agent
from .q_function import Linear_Q


def main(args):
    height, width = args.dims
    score1 = 0
    score2 = 0
    num_ties = 0
    win1 = 0
    win2 = 0
    for epoch in range(args.epochs):
        state_data = []
        action_data = []
        reward_data = []
        board = Board(height, width)
        agent1 = Agent(board, 0, True)
        agent2 = Agent(board, 0, False)
        i = 0
        while i < len(board.sides):
            i += 1
            if agent1.turn:
                counts_before, _ = board.squares_stat()
                state_data.append(counts_before)
                agent1.decide()
                action_data.append([agent1.action])
                if not agent1.turn:
                    agent2.set_turn(True)
                    reward_data.append([0])
                else:
                    reward_data.append([1])
            elif agent2.turn:
                agent2.decide()
                if not agent2.turn:
                    agent1.set_turn(True)
                    reward_data.append([0])
                else:
                    reward_data.append([-1])
        if agent1.reward > agent2.reward:
            agent1.add_reward(100)
            win1 += 1
        elif agent1.reward < agent2.reward:
            agent2.add_reward(100)
            win2 += 1
        else:
            num_ties += 1
        score1 += agent1.reward
        score2 += agent2.reward
    print(score1, score2)
    print(f"1 wins {win1} times, 2 wins {win2} times, tie {num_ties} times")
    print(len(reward_data))
    print(len(action_data), action_data)
    print(len(state_data), state_data)
