from abc import ABC, abstractmethod
from game.utils import is_prime_trial_division


class Strategy(ABC):
    @abstractmethod
    def generate_message(self, num: int) -> str:
        pass


class FizzBuzzStrategy(Strategy):
    def generate_message(self, num: int) -> str:
        if num % 3 == 0 and num % 5 == 0:
            return "FizzBuzz"
        elif num % 3 == 0:
            return "Fizz"
        elif num % 5 == 0:
            return "Buzz"
        return str(num)


class PrimeBarStrategy(Strategy):
    def generate_message(self, num: int) -> str:
        if is_prime_trial_division(num):
            return "Foo"
        elif str(num)[-1] == "4":
            return "Bar"
        return str(num)


class StrategyRegistry:
    _strategies: dict[str, Strategy] = {
        "FizzBuzz": FizzBuzzStrategy(),
        "PrimeBar": PrimeBarStrategy(),
    }

    @classmethod
    def get_strategy(cls, strategy_name: str) -> Strategy:
        return cls._strategies.get(strategy_name, FizzBuzzStrategy())
