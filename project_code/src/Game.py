import random
from typing import List

class Character:
    def __init__(self, name: str = None):
        self.name = self._generate_name() if name is None else name

    def _generate_name(self):
        return "Bob"

class Driver(Character):
    def __init__(self, level: int = 1):
        super().__init__()
        self.level = level

    def upgrade(self):
        if self.level < 4:
            self.level += 1

    def randomize_level(self):
        self.level = random.randint(1, 4)

class Pit_crew(Character):
    def __init__(self, level: int = 1):
        super().__init__()
        self.level = level

    def upgrade(self):
        if self.level < 4:
            self.level += 1

    def pit_stop_time(self):
        if self.level == 1:
            return round(random.uniform(10, 15), 1)
        elif self.level == 2:
            return round(random.uniform(6, 10), 1)
        elif self.level == 3:
            return round(random.uniform(4, 8), 1)
        elif self.level == 4:
            return round(random.uniform(2, 3.5), 1)

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

class Player_car:
    def __init__(self):
        self.level = 1

    def upgrade(self):
        if self.level < 4:
            self.level += 1

class Opponent_car:
    def __init__(self):
        self.level = 1

    def randomize_level(self):
        self.level = random.randint(1, 4)

class Location:
    def __init__(self, name: str):
        self.name = name

class Event:
    def __init__(self, name: str):
        self.name = name

    def handle_event(self, race=None):
        if self.name == 'Race start':
            print("The race has started!")
        elif self.name == 'Straight battle':
            race.car.performance -= 1
            print(f"Straight battle occurred. Car performance decreased to {race.car.performance}")
        elif self.name == 'High speed corner battle':
            race.car.performance -= 2
            print(f"High speed corner battle occurred. Car performance decreased to {race.car.performance}")
        elif self.name == 'Medium speed corner battle':
            race.car.performance -= 1
            race.driver.stamina -= 1
            print(f"Medium speed corner battle occurred. Car performance and driver stamina decreased.")
        elif self.name == 'Low speed corner battle':
            race.driver.stamina -= 2
            print(f"Low speed corner battle occurred. Driver stamina decreased to {race.driver.stamina}")
        elif self.name == 'Pit stop':
            race.car.performance += 1
            race.driver.stamina += 1
            print("Pit stop occurred. Car performance and driver stamina increased.")
        else:
            print("Unknown event occurred.")

class Game:
    def __init__(self):
        self.characters: List[Character] = [Driver(), Pit_crew(), Engineers()]
        self.locations: List[Location] = [Location("British Grand Prix"), Location("Italian Grand Prix")]
        self.events: List[Event] = [Event(name) for name in ['Race Start', 'Straight battle', 'High-speed corner battle',
                                                             'Medium-speed corner battle',
                                                             'Low-speed corner battle', 'Pit stop', "Safety car", 'Crash', 'Race finish']]
        self.party: List[Character] = [Character(name='Team Owner')]
        self.current_location = None
        self.current_event = None
        self.continue_playing = True

    def upgrade_menu(self, player_driver: Driver, player_car: Player_car, player_pit_crew: Pit_crew):
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

    def parse_input(self, user_input: str):
        command = user_input.strip().lower()
        return command

    def update_game_state(self, command):
        if command == 'upgrade driver':
            self.characters[0].upgrade()  # Assuming the driver is the first character in the list
        elif command == 'upgrade pit crew':
            self.characters[1].upgrade()  # Assuming the pit crew is the second character in the list
        elif command == 'upgrade engineers':
            self.characters[2].upgrade()  # Assuming the engineers are the third character in the list
        elif command == 'end game':
            self.end_game()
        else:
            print(f"Unknown command: {command}")

    def is_party_dead(self):
        return all(character.level == 1 for character in self.characters)

    def award_legacy_points(self):
    # Award legacy points based on the levels of the characters
        legacy_points = sum(character.level for character in self.characters)
        print(f"You have been awarded {legacy_points} legacy points!")

    def end_game(self):
    # End the game
        self.continue_playing = False
        print("The game has ended. Thank you for playing!")

if __name__ == "__main__":
    game = Game()
    num_races = 5  # Championship consists of 5 races
    player_driver = Driver()  # Player's driver starts at level 1
    player_car = Player_car()  # Player's car starts at level 1
    player_pit_crew = Pit_crew()  # Player's pit crew starts at level 1

    for race in range(num_races):
        print(f"\nRace {race + 1}")
        game.upgrade_menu(player_driver, player_car, player_pit_crew)