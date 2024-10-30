from game.player import PlayerFactory
from game.strategies import StrategyRegistry
from game.output import OutputRegistry, OutputType
from game.game import Game
from ui.user_interface import UserInterface


def main() -> None:
    # Get user input for player 2's output type
    output_options = {o.value: o.name for o in OutputType}
    selected_type_player2 = OutputType(
        UserInterface.get_user_input("Select game output:", output_options)
    )

    # Create players with strategies and outputs
    player1 = PlayerFactory.create_player(
        "Player1",
        StrategyRegistry.get_strategy("PrimeBar"),
        OutputRegistry.get_output(OutputType.CONSOLE),
    )
    player2 = PlayerFactory.create_player(
        "Player2",
        StrategyRegistry.get_strategy("FizzBuzz"),
        OutputRegistry.get_output(selected_type_player2),
    )

    # Initialize and start the game
    game = Game([player1, player2])
    game.play(100)


if __name__ == "__main__":
    main()
