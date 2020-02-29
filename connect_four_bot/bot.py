import gym
import tensorflow as tf
from random import shuffle
from numpy import argsort

from connect_four_bot.envs import ConnectFourEnv
from connect_four_bot.linearmodel import Linear


class ConnectFourBotRandom(gym.Env):
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

class ConnectFourBotNN(gym.Env):
    """
    Description:
        ConnectFour game bot
    """
    def __init__(self):
        self.board = ConnectFourEnv()
        self.NN = Linear()

    def nextMove(self):
        boardvalues = self.board.board.flatten()
        mytensor = tf.constant(boardvalues, dtype='float32')
        x = self.NN([mytensor])
        available_moves = self.board.available_moves()
        for i in reversed(argsort(x)):
            if i in available_moves:
                return i

    def inform(self, action):
        self.board.step(action)