from .train_utils import map_side_to_square, calc_squares_status
from .train_utils import Board, Agent
from .q_function import Linear_Q
import torch
import numpy as np
import matplotlib.pyplot as plt


def main(args):
    height, width = args.dims
    score1 = 0
    score2 = 0
    num_ties = 0
    win1 = 0
    win2 = 0
    criterion = torch.nn.MSELoss()
    model = Linear_Q(6)
    optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)
    loss_list = []
    for epoch in range(args.epochs):
        running_loss = 0
        optimizer.zero_grad()
        action_data = []
        state_data = []
        full_action_data = []
        reward_data = []
        next_state_data = []
        delta_data = []
        board = Board(height, width)
        agent1 = Agent(board, 0, True)
        agent2 = Agent(board, 0, False)
        i = 0
        agg_reward = []
        agg_reward_previous = 0
        while i < len(board.sides):
            i += 1
            if agent1.turn:
                counts_before, _ = board.squares_stat()
                state_data.append(counts_before)
                if i > 1:
                    agg_reward.append(agg_current_reward)
                agg_current_reward = 0
                agent1.decide(args.playmode[0])

                full_action_data.append([agent1.action])
                counts_after, _ = board.squares_stat()
                next_state_data.append(counts_after)

                ddata = [a-b for (a, b) in zip(counts_after, counts_before)]
                what_changed = next((i for i, x in enumerate(ddata) if x < 0))
                action_data.append(what_changed)
                delta_data.append(ddata)
                if not agent1.turn:
                    agent2.set_turn(True)
                    reward_data.append(['a', 0])
                    agg_current_reward += 0
                else:
                    reward_data.append(['a', 1])
                    agg_current_reward += 1
            elif agent2.turn:
                agent2.decide(args.playmode[1])
                if not agent2.turn:
                    agent1.set_turn(True)
                    reward_data.append(['b', 0])
                    agg_current_reward += 0
                else:
                    reward_data.append(['b', -1])
                    agg_current_reward += -1
            agg_reward_after = agent1.reward - agent2.reward
        agg_reward.append(agg_current_reward)

        input_array = torch.from_numpy(np.concatenate(
            (np.array(state_data), np.array(np.expand_dims(action_data, axis=1))), axis=1)).type(torch.FloatTensor)

        target_array = torch.tensor(
            agg_reward, dtype=torch.float).type(torch.FloatTensor)
        output_array = model(input_array).squeeze()
        loss = criterion(target_array, output_array)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
        #print(f"Running loss at epoch {epoch} is {running_loss}")
        loss_list.append(running_loss)

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
    print(len(reward_data), reward_data)

    print("f", full_action_data, len(state_data), agent1.action_list)
    #print("state: ", len(state_data), state_data)
    #print("next state: ", len(next_state_data), next_state_data)
    print(len(delta_data), delta_data)
    print(len(agg_reward), agg_reward)
    print(len(action_data), action_data)
    print(list(zip(action_data, agg_reward)))
    avg_window_len = 100
    loss_list_avg = [sum(loss_list[i:i+avg_window_len]) /
                     avg_window_len for i in range(args.epochs-avg_window_len)]
    #plt.plot(range(args.epochs-avg_window_len), loss_list_avg)
    # plt.show()
