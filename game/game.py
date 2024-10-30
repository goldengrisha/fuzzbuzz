from typing import List
from game.player import Player


class Game:
    def __init__(self, players: List[Player]):
        self.players = players

    def play(self, rounds: int) -> None:
        for i in range(1, rounds + 1):
            for player in self.players:
                player.play(i)
