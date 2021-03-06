from typing import Tuple, Optional

import gym
import numpy as np

class ConnectFourEnv(gym.Env):
    """
    Description:
        ConnectFour game environment

    Observation:
        Type: Discreet(6,7)

    Actions:
        Type: Discreet(7)
        Num     Action
        x       Column in which to insert next token (0-6)

    Reward:
        Reward is 0 for every step.
        If there are no other further steps possible, Reward is 0.5 and termination will occur
        If player "1" wins, reward is 1 and termination occurs
        If player "-1" wins, reward is -1 and termination occurs

    Starting State:
        All observations are assigned a value of 0

    Episode Termination:
        No more spaces left for pieces
        4 pieces are present in a line: horizontal, vertical or diagonally
        An attempt is made to place a piece in an invalid location
    """

    def __init__(self, board_shape=(6, 7), window_width=512, window_height=512):
        super(ConnectFourEnv, self).__init__()

        self.board_shape = board_shape
        self.__board = np.zeros(self.board_shape, dtype=int)

        self._current_player = 1
        self._winner = 0

    @property
    def board(self):
        return self.__board.copy()

    def available_moves(self) -> frozenset:
        return frozenset(
            (i for i in range(self.board_shape[1]) if self.is_valid_action(i))
        )

    def step(self, action: int) -> Tuple[np.ndarray, float, bool, dict]:
        # check input
        if not self.is_valid_action(action):
            raise Exception(
                "Unable to determine a valid move! Maybe invoke at the wrong time?"
            )
        # perform action
        for index in list(reversed(range(self.board_shape[0]))):
            if self.__board[index][action] == 0:
                self.__board[index][action] = self._current_player
                break
        # 'done' if there is either a winner, or no further moves available
        done = self.is_win_state() or (self.available_moves() == set())
        # check if this action lead to a winner
        if (self._winner == 0) and self.is_win_state():
            self._winner = self._current_player
        # calculate reward (ongoing: 0, player 1 won: 1, player -1 won: -1, draw: 0.5)
        reward = self._winner
        if done and (self._winner == 0):
            reward = 0.5
        # change player (for next turn)
        self._current_player *= -1
        # return tuple
        return self.__board.copy(), reward, done, {}

    def is_valid_action(self, action: int) -> bool:
        return self.__board[0][action] == 0

    def is_win_state(self) -> bool:
        # Test rows
        for i in range(self.board_shape[0]):
            for j in range(self.board_shape[1] - 3):
                value = sum(self.__board[i][j : j + 4])
                if abs(value) == 4:
                    return True

        # Test columns on transpose array
        reversed_board = [list(i) for i in zip(*self.__board)]
        for i in range(self.board_shape[1]):
            for j in range(self.board_shape[0] - 3):
                value = sum(reversed_board[i][j : j + 4])
                if abs(value) == 4:
                    return True

        # Test diagonal
        for i in range(self.board_shape[0] - 3):
            for j in range(self.board_shape[1] - 3):
                value = 0
                for k in range(4):
                    value += self.__board[i + k][j + k]
                    if abs(value) == 4:
                        return True

        reversed_board = np.fliplr(self.__board)
        # Test reverse diagonal
        for i in range(self.board_shape[0] - 3):
            for j in range(self.board_shape[1] - 3):
                value = 0
                for k in range(4):
                    value += reversed_board[i + k][j + k]
                    if abs(value) == 4:
                        return True

        return False

    def reset(self, board: Optional[np.ndarray] = None) -> np.ndarray:
        self._current_player = 1
        if board is None:
            self.__board = np.zeros(self.board_shape, dtype=int)
        else:
            self.__board = board
        return self.board
