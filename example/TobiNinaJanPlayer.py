""" Player implementation for TobiNinaJan"""

from py_client.players import Player


class TobiNinaJanPlayer(Player):
    def __init__(self, player):
        self._player = player

    def choose_action(self) -> int:
        return self._player.nextMove()

    def inform(self, column: int, opponent: bool):
        # Tobi said that the information about the player can be dropped --
        # as long as the order of the messages is alright. Let's just assume
        # that it is.
        self._player.inform(column)

    def reset(self):
        self._player.reset()