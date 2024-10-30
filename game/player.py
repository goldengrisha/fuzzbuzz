from game.strategies import Strategy
from game.output import BaseOutput


class Player:
    def __init__(self, name: str, strategy: Strategy, output: BaseOutput):
        self.name = name
        self.strategy = strategy
        self.output = output

    def play(self, num: int) -> None:
        message = f"{self.name}: {self.strategy.generate_message(num)}"
        self.output.process(message)


class PlayerFactory:
    @staticmethod
    def create_player(name: str, strategy: Strategy, output: BaseOutput) -> Player:
        return Player(name, strategy, output)
