from typing import Dict


class UserInterface:
    @staticmethod
    def get_user_input(prompt: str, options: Dict[int, str]) -> int:
        """
        Prompt the user to select an option.

        :param prompt: The prompt message to display to the user.
        :param options: A dictionary mapping option numbers to their descriptions.
        :return: The selected option as an integer.
        """
        print(prompt)
        for key, description in options.items():
            print(f"  {key}. {description}")

        user_input = None
        while user_input not in options:
            try:
                user_input = int(input("Enter your choice: "))
                if user_input not in options:
                    print("Invalid selection. Please choose a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        return user_input
