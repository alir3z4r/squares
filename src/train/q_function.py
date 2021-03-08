import torch
import torch.nn as nn


class Linear_Q(nn.Module):
    def __init__(self, num_unique_squares):
        super(Linear_Q, self).__init__()
        self.num_unique_squares = num_unique_squares
        self.linear_model = nn.Linear(num_unique_squares, 1)

    def forward(self, x):
        return self.linear_model(x)
