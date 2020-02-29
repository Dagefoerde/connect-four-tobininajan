from typing import Tuple, Optional

import gym
import numpy as np
from random import shuffle

from connect_four_bot.envs import ConnectFourEnv

class ConnectFourBot(gym.Env):
    """
    Description:
        ConnectFour game bot
    """
    def __init__(self):
        self.board = ConnectFourEnv()

    def nextMove(self):
        x = list(self.board.available_moves())
        shuffle(x)
        return x[0]

    def inform(self, action):
        self.board.step(action)