from enum import Enum
from abc import ABC, abstractmethod


class OutputType(Enum):
    CONSOLE = 1
    EMAIL = 2


class BaseOutput(ABC):
    @abstractmethod
    def process(self, message: str) -> None:
        pass


class ConsoleOutput(BaseOutput):
    def process(self, message: str) -> None:
        print(f"console: {message}")


class EmailOutput(BaseOutput):
    def process(self, message: str) -> None:
        print(f"email: {message}")


class OutputRegistry:
    _outputs: dict[OutputType, BaseOutput] = {
        OutputType.CONSOLE: ConsoleOutput(),
        OutputType.EMAIL: EmailOutput(),
    }

    @classmethod
    def get_output(cls, output_type: OutputType) -> BaseOutput:
        return cls._outputs.get(output_type, ConsoleOutput())
