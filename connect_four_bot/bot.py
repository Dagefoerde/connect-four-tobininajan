from typing import Tuple, Optional

import gym
import numpy as np

from connect_four_bot.envs import ConnectFourEnv

class ConnectFourBot(gym.Env):
    """
    Description:
        ConnectFour game bot
    """
    def __init__(self):
        self.board = ConnectFourEnv()

    def nextMove(self):
        return list(self.board.available_moves())[0]

    def inform(self, action):
        self.board.step(action)