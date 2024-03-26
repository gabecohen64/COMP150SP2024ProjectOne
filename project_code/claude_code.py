import random
from typing import List

class Character:
    def __init__(self, name: str = None):
        self.name = self._generate_name() if name is None else name

    def _generate_name(self):
        return "Bob"

class Driver(Character):
    def __init__(self, level):
        super().__init__()
        self.level = level

    def upgrade(self):
        if self.level < 4:
            self.level += 1

    def randomize_level(self):
        self.level = random.randint(1, 4)

class Pit_crew(Character):
    def __init__(self, level):
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
    def __init__(self):
        super().__init__()

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
    def __init__(self, name):
        self.name = name

class Event:
    pass

class Game:
    def __init__(self):
        self.characters: List[Character] = [Driver(1), Pit_crew(1), Engineers()]
        self.locations: List[Location] = [Location("British Grand Prix"), Location("Italian Grand Prix")]
        self.events: List[Event] = ["Race Start", "Straight battle", "High-speed corner battle",
                                    "Medium-speed corner battle",
                                    "Low-speed corner battle", "Pit stop", "Safety car", "Crash", "Race finish"]
        self.party: List[Character] = ["Team Owner"]
        self.current_location = None
        self.current_event = None
        self.continue_playing = True

    def upgrade_menu(self, player_driver, player_car, player_pit_crew):
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
        else:
            print("Invalid choice!")

class Race:
    def __init__(self):
        self.events = ['Straight battle', 'High speed corner battle', 'Medium speed corner battle',
                       'Low speed corner battle', 'Pit stop']

    def get_race_name(self):
        race_names = ["British Grand Prix", "Italian Grand Prix", "Monaco Grand Prix", "Brazilian Grand Prix",
                      "Belgian Grand Prix"]
        return random.choice(race_names)

    def race_start(self):
        if random.random() < 0.9:
            print("Race start successful!")
            return True
        else:
            print("DNF. You crashed with another driver and are out of this race.")
            return False

    def straight_battle(self, player_driver, player_car, opponent_driver, opponent_car):
        if random.random() < 0.025:
            print("DNF. You crashed trying a straight line overtake.")
            return "DNF"

        opponent_driver.randomize_level()
        opponent_car.randomize_level()

        if player_driver.level >= 3 and player_car.level == opponent_car.level:
            print("Straight line overtake successful!")
            return "Player's car"
        elif player_car.level > opponent_car.level:
            print("Straight line overtake successful!")
            return "Player's car"
        elif player_car.level == opponent_car.level:
            print("Straight line overtake failed.")
            return "Opponent's car"
        else:
            print("Straight line overtake failed.")
            return "Opponent's car"

    def low_speed_corner_battle(self, player_driver, opponent_driver):
        if random.random() < 0.05:
            print("DNF. You crashed trying a low speed corner overtake.")
            return "DNF"

        opponent_driver.randomize_level()

        if player_driver.level > opponent_driver.level:
            print("Low speed corner overtake successful!")
            return "Player's car"
        elif player_driver.level == opponent_driver.level:
            print("Low speed corner overtake failed.")
            return "Opponent's car"
        else:
            print("Low speed corner overtake failed.")
            return "Opponent's car"

    def medium_speed_corner_battle(self, player_driver, player_car, opponent_driver, opponent_car):
        if random.random() < 0.1:
            print("DNF. You crashed trying a medium speed corner overtake.")
            return "DNF"

        opponent_driver.randomize_level()
        opponent_car.randomize_level()

        player_strength = (player_driver.level + player_car.level) / 2
        opponent_strength = (opponent_driver.level + opponent_car.level) / 2
        if player_strength > opponent_strength:
            print("Medium speed corner overtake successful!")
            return "Player's car"
        elif player_strength == opponent_strength:
            print("Medium speed corner overtake failed.")
            return "Opponent's car"
        else:
            print("Medium speed corner overtake failed.")
            return "Opponent's car"

    def high_speed_corner_battle(self, player_driver, player_car, opponent_driver, opponent_car):
        if random.random() < 0.15:
            print("DNF. You crashed trying a high speed corner overtake.")
            return "DNF"
        opponent_driver.randomize_level()
        opponent_car.randomize_level()

        player_strength = (player_driver.level * 0.25) + (player_car.level * 0.75)
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

    def pit_stop(self, player_pit_crew):
        pit_time = player_pit_crew.pit_stop_time()
        print(f"Player's pit stop time: {pit_time} seconds")

        return pit_time

def run_race(game, player_driver, player_car, player_pit_crew):
    race = Race()
    opponent_driver = Driver(1)
    opponent_car = Opponent_car()

    if not race.race_start():
        return

    race_name = race.get_race_name()
    print(f"\nRace: {race_name}")

    print("Race started!")
    print(f"Player's driver level: {player_driver.level}, Player's car level: {player_car.level}")

    events = [race.straight_battle, race.low_speed_corner_battle, race.medium_speed_corner_battle,
              race.high_speed_corner_battle, race.pit_stop] * 2

    random.shuffle(events)

    for event in events:
        if event == race.pit_stop:
            event(player_pit_crew)
        else:
            event_outcome = event(player_driver, player_car, opponent_driver, opponent_car)

            if event_outcome == "DNF":
                break

    print("Race finish!")

if __name__ == "__main__":
    game = Game()
    num_races = 5
    player_driver = Driver(1)
    player_car = Player_car()
    player_pit_crew = Pit_crew(1)

    for race in range(num_races):
        print(f"\nRace {race + 1}")
        game.upgrade_menu(player_driver, player_car, player_pit_crew)
        run_race(game, player_driver, player_car, player_pit_crew)