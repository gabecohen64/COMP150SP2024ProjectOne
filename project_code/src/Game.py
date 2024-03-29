class Engineers(Character):
    def __init__(self, name: str = None, skill_level: int = 1):
        super().__init__(name)
        self.skill_level = skill_level

    def upgrade_skill(self):
        self.skill_level += 1

    def perform_action(self):
        # Increase the performance of the car
        self.upgrade_car_performance()

    def upgrade_car_performance(self):
        # Increase the skill level of the engineer, which in turn increases the performance of the car
        self.skill_level += 1
        print(f"Car performance upgraded by engineer {self.name}. Current skill level: {self.skill_level}")


class Game:
    def __init__(self):
        self.characters: List[Character] = [Driver(1), Pit_crew(1), Engineers()]
        self.locations: List[Location] = [Location('British Grand Prix'), Location('Italian Grand Prix')]
        self.events: List[Event] = ['Race Start', 'Straight battle', 'High-speed corner battle',
                                    'Medium-speed corner battle',
                                    'Low-speed corner battle', 'Pit stop', "Safety car", 'Crash', 'Race finish']
        self.party: List[Character] = ['Team Owner']
        self.current_location = None
        self.current_event = None
        self._initialize_game()
        self.continue_playing = True

    def upgrade_menu(self, player_driver, player_car, player_pit_crew):
        while True:
            print("\nUpgrade Menu:")
            print("1. Upgrade Driver")
            print("2. Upgrade Car")
            print("3. Upgrade Pit Crew")
            print("4. Continue to next race")

            choice = input("Enter your choice (1-4): ")
            if choice == "1":
                player_driver.upgrade()
                print("Driver upgraded!")
            elif choice == "2":
                player_car.upgrade()
                print("Car upgraded!")
            elif choice == "3":
                player_pit_crew.upgrade()
                print("Pit Crew upgraded!")
            elif choice == "4":
                print("Continuing to next race...")
                break
            else:
                print("Invalid choice!")

    def _main_game_loop(self):
        """The main game loop."""
        while self.continue_playing:
            user_input = input("Enter your command: ")
            command = self.parse_input(user_input)
            self.update_game_state(command)
            if self.is_party_dead():
                # If party is dead, award legacy points and end instance of game
                self.award_legacy_points()
                self.end_game()
            else:
                continue

            if self.continue_playing is False:
                return True
            elif self.continue_playing == "Save and quit":
                return "Save and quit"
            else:
                return False
if __name__ == "__main__":
    game = Game()
    num_races = 5  # Championship consists of 5 races
    player_driver = Driver()  # Player's driver starts at level 1
    player_car = Player_car()  # Player's car starts at level 1
    player_pit_crew = Pit_crew(1)  # Player's pit crew starts at level 1

    for race in range(num_races):
        print(f"\nRace {race + 1}")
        game.upgrade_menu(player_driver, player_car, player_pit_crew)