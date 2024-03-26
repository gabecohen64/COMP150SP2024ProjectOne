from project_code.src.Game import Game

class User:
    def __init__(self, username: str, password: str, legacy_points: int = 0):
        self.username = username
        self.password = password
        self.legacy_points = legacy_points
        self.current_game = self._get_or_create_game()

    def _get_or_create_game(self) -> Game:
        # Here you can implement logic to retrieve a saved game state if available,
        # or create a new game if no saved state is found.
        return Game()

    def save_game(self):
        # Placeholder method to save the game state
        # You can implement saving game state to a file or database here
        print("Saving game state...")
        # Example: save game state to a file
        with open("saved_game_state.txt", "w") as file:
            file.write("Game state saved successfully.")
        print("Game state saved successfully.")
