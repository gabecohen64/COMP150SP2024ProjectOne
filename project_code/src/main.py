import random
from typing import List

class Character:
    def __init__(self, name: str = None):
        self.level = None
        self.name = self._generate_name() if name is None else name

    def _generate_name(self):
        return "Bob"

class Driver(Character):
    def __init__(self, level):
        super().__init__()
        self.level = level
        self.stamina = 100  # New attribute for driver's stamina

    def upgrade(self):
        if self.level < 4:
            self.level += 1

    def randomize_level(self):
        self.level = random.randint(3, 4)  # Adjusted to give player's driver higher level

class Pit_crew(Character):
    def __init__(self, level):
        super().__init__()
        self.level = level

    def upgrade(self):
        if self.level < 4:
            self.level += 1

    def pit_stop_time(self):
        if self.level == 1:
            return round(random.uniform(8, 12), 1)  # Decreased pit stop time for player's advantage
        elif self.level == 2:
            return round(random.uniform(5, 8), 1)  # Decreased pit stop time for player's advantage
        elif self.level == 3:
            return round(random.uniform(3, 6), 1)  # Decreased pit stop time for player's advantage
        elif self.level == 4:
            return round(random.uniform(1, 3), 1)  # Decreased pit stop time for player's advantage

class Engineers(Character):
    def __init__(self):
        super().__init__()

class Player_car:
    def __init__(self):
        self.level = 1
        self.performance = 100  # New attribute for car's performance

    def upgrade(self):
        if self.level < 4:
            self.level += 1

class Opponent_car:
    def __init__(self):
        self.level = 1
        self.performance = 100  # New attribute for opponent car's performance

    def randomize_level(self):
        self.level = random.randint(1, 2)  # Decreased opponent's car level to make the game easier

class Location:
    def __init__(self, name):
        self.name = name

class Event:
    def __init__(self, name):
        self.name = name

    def handle_event(self, race=None):
        if self.name == 'Race start':
            print("The race has started!")
        elif self.name == 'Straight battle':
            race.player_car.performance -= 1
            print(f"Straight battle occurred. Car performance decreased to {race.player_car.performance}")
        elif self.name == 'High speed corner battle':
            race.player_car.performance -= 1
            print(f"High speed corner battle occurred. Car performance decreased to {race.player_car.performance}")
        elif self.name == 'Medium speed corner battle':
            race.player_car.performance -= 1
            print(f"Medium speed corner battle occurred. Car performance decreased to {race.player_car.performance}")
        elif self.name == 'Low speed corner battle':
            race.player_car.performance -= 1
            print(f"Low speed corner battle occurred. Car performance decreased to {race.player_car.performance}")
        elif self.name == 'Pit stop':
            race.player_car.performance += 2  # Increased performance boost from pit stop
            print("Pit stop occurred. Car performance increased.")
        else:
            print("Unknown event occurred.")

class Game:
    def __init__(self):
        self.characters: List[Character] = [Driver(4), Pit_crew(4), Engineers()]  # Increased initial levels for player
        self.player_car = Player_car()  # Moved Player_car instance to Game
        self.locations: List[Location] = [Location("British Grand Prix"), Location("Italian Grand Prix")]
        self.events: List[Event] = [Event("Race Start"), Event("Straight battle"), Event("High-speed corner battle"),
                                    Event("Medium-speed corner battle"),
                                    Event("Low-speed corner battle"), Event("Pit stop")]
        self.party: List[Character] = [Character("Team Owner")]
        self.current_location = None
        self.current_event = None
        self.continue_playing = True
        self.score = 0

    def start_game(self):
        print("Welcome to the game!")
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        character_name = input("Please enter your character's name: ")

        # You can use the username, password, and character_name here
        # For example, you might want to create a new Character with the given name
        self.characters.append(Character(name=character_name))

    def upgrade_menu(self, player_driver, player_pit_crew):
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
            self.player_car.upgrade()
            print("Car upgraded!")
        elif choice == "3":
            player_pit_crew.upgrade()
            print("Pit Crew upgraded!")
        elif choice == "4":
            print("Continuing to next race...")
        else:
            print("Invalid choice!")

    def update_score(self, outcome):
        if outcome == "Player's car":
            self.score += 2  # Increase the score for player's win
        elif outcome == "Opponent's car":
            self.score -= 1  # Reduce the penalty for opponent's win

    def check_game_over(self):
        if self.score <= -5:  # Adjust the game over threshold
            print("Game Over. You lost the championship now go eat nachos and cry.")
            self.continue_playing = False
        elif self.score >= 5:
            print("Congratulations! You won the championship.")
            self.continue_playing = False

def get_race_name():
    race_names = ["British Grand Prix", "Italian Grand Prix", "Monaco Grand Prix", "Brazilian Grand Prix",
                  "Belgian Grand Prix"]
    return random.choice(race_names)

class Race:
    def __init__(self, game: Game):
        self.game = game
        self.events = [event.name for event in game.events]
        self.player_driver = game.characters[0]
        self.player_pit_crew = game.characters[1]

    def race_start(self):
        if random.random() < 0.9:
            print("Race start successful!")
            return True
        else:
            print("You crashed with another driver and are out of this race, NOW GO HOME.")
            return False

    def straight_battle(self, opponent_driver, opponent_car):
        if random.random() < 0.025:
            print("You crashed trying a straight line overtake but still go on.")

        opponent_driver.randomize_level()
        opponent_car.randomize_level()

        if self.player_driver.level >= 3:
            if self.game.player_car.level >= opponent_car.level:
                print("Straight line overtake successful!")
                return "Player's car"
            else:
                print("Straight line overtake failed.")
                return "Opponent's car"
        elif self.game.player_car.level > opponent_car.level:
            print("Straight line overtake successful!")
            return "Player's car"
        else:
            print("Straight line overtake failed.")
            return "Opponent's car"

    def low_speed_corner_battle(self, opponent_driver):
        if random.random() < 0.05:
            print("C'MON, You crashed trying a low speed corner overtake SERIOUSLY.")
            return "BOOHOO"
        opponent_driver.randomize_level()
        if self.player_driver.level > opponent_driver.level:
            print("Low speed corner overtake successful!")
            return "Player's car"
        elif self.player_driver.level == opponent_driver.level:
            print("Low speed corner overtake failed.")
            return "Opponent's car"
        else:
            print("Low speed corner overtake failed.")
            return "Opponent's car"

    def medium_speed_corner_battle(self, opponent_driver, opponent_car):
        if random.random() < 0.1:
            print("You crashed trying a medium speed corner overtake.")
            return "Moves down 2 positions on the board"
        opponent_driver.randomize_level()
        opponent_car.randomize_level()

        player_strength = (self.player_driver.level + self.game.player_car.level) / 2
        opponent_strength = (opponent_driver.level + opponent_car.level) / 2
        if player_strength > opponent_strength:
            print("Medium speed corner overtake successful, LETS GO!")
            return "Player's car"
        elif player_strength == opponent_strength:
            print("Medium speed corner overtake failed how sad.")
            return "Opponent's car"
        else:
            print("Medium speed corner overtake failed keep trying lad.")
            return "Opponent's car"

    def high_speed_corner_battle(self, opponent_driver, opponent_car):
        if random.random() < 0.15:
            print("OOF, You crashed trying a high speed corner overtake but you are coming back fast my flashy friend.")
        opponent_driver.randomize_level()
        opponent_car.randomize_level()

        player_strength = (self.player_driver.level * 0.25) + (self.game.player_car.level * 0.75)
        opponent_strength = (opponent_driver.level * 0.25) + (opponent_car.level * 0.75)
        if player_strength > opponent_strength:
            print("High speed corner overtake successful!")
            return "Player's car"
        elif player_strength == opponent_strength:
            print("High speed corner overtake failed.")
            return "Opponent's car"
        else:
            print("High speed corner overtake failed.")
            return "Opponent's car"

    def pit_stop(self):
        pit_time = self.player_pit_crew.pit_stop_time()
        print(f"Player's pit stop time: {pit_time} seconds")

        return pit_time

def run_race(game: Game):
    race = Race(game)
    opponent_driver = Driver(1)
    opponent_car = Opponent_car()
    if not race.race_start():
        return

    race_name = get_race_name()
    print(f"\nRace: {race_name}")

    print("Race started!")
    print(f"Player's driver level: {race.player_driver.level}, Player's car level: {game.player_car.level}")

    events = [race.straight_battle, race.low_speed_corner_battle, race.medium_speed_corner_battle,
              race.high_speed_corner_battle, race.pit_stop] * 2

    random.shuffle(events)

    for event in events:
        event_outcome = None
        if event == race.pit_stop:
            event_outcome = event()
        elif event == race.low_speed_corner_battle:
            event_outcome = event(opponent_driver)
        else:
            event_outcome = event(opponent_driver, opponent_car)

        if event_outcome in ["Player's car", "Opponent's car"]:
            game.update_score(event_outcome)

        if event_outcome == "DNF" or not game.continue_playing:
            break

    print("Race finish!")
    game.check_game_over()

if __name__ == "__main__":
    game = Game()
    game.start_game()
    num_races = 4

    for race in range(num_races):
        print(f"\nRace {race + 1}")
        game.upgrade_menu(game.characters[0], game.characters[1])
        run_race(game)
        if not game.continue_playing:
            break
