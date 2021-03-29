import torch as T
import torch.nn as nn
import torch.nn.functional as F


class Linear_Q(nn.Module):
    def __init__(self, num_unique_squares):
        super(Linear_Q, self).__init__()
        self.num_unique_squares = num_unique_squares
        self.linear_model = nn.Linear(num_unique_squares, 1)

    def forward(self, x):
        return self.linear_model(x)

class DeepQN(nn.Module):
    def __init__(self, replay_memory, layers):
        super(DeepQN, self).__init__()
        self.replay_memory = replay_memory
        self.layers = layers
        self.fc_list = ModuleList([nn.Linear(self.layers[i], self.layers[i+1]) for i in range(len(layers-1))])

    def forward(self, x):
        for i in range(len(self.layers)-1):
            x = F.relu(self.fc_list[i](x))
        x = self.fc_list[-1](x)
        return x

