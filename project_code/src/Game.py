'''game ideas: racing theme, characters are drivers, pit crew members, engineers, and team boss. these characters can receive upgrades. upgraded drivers are faster and more consistent meaning less incidents 
 like spinning out or crashing. upgraded pit crews add more pit crew members per upgrade, meaning faster pit stops. upgraded engineers mean a faster car with upgraded aerodynamics and engine. an upgraded
boss adds more consistency to pit stops and car upgrades. a lower level boss increases the chances of inconsistent pit stop times regardless of the number of members, and it can mean car upgrades may backfire
and make the car slower than before. events could be the race start, pit stops, and battles on sections of track such as straights, high speed, medium speed, and low speed corners. include safety car as cutscene.
safety car is most common pit stop time.'''

from typing import List

from project_code.src.Character import Character
from project_code.src.Event import Event
from project_code.src.Location import Location


class Game:
    def __init__(self):
        self.characters: List[Character] = ["Driver", "Pit crew", "Engineers"]
        self.locations: List[Location] = ["Race Track"]
        self.events: List[Event] = ["Race Start", "Straight battle", "High-speed corner battle", "Medium-speed corner battle", 
        "Low-speed corner battle", "Pit stop", "Safety car", "Crash", "Race finish"]
        self.party: List[Character] = ["Team Owner"]
        self.current_location = None
        self.current_event = None
        self._initialize_game()
        self.continue_playing = True

# Initalizes all upgrades and set race number to 1 before championship starts
class Character:
    def __init__(self, level=1):
        self.level = level

class Driver(Character):
    pass

class Pit_crew(Character):
    pass

class Engineers(Character):
    pass

class Race:
    def __init__(self):
        self.number = 1

def initialize_levels():
    driver = Driver()
    pit_crew = Pit_crew()
    engineers = Engineers()
    return driver, pit_crew, engineer

# Randomizing the order of races in the championship as well as defining the number of events per race
class Race:
    RACE_NAMES = [
        "British Grand Prix",
        "Monaco Grand Prix",
        "Brazilian Grand Prix",
        "Belgian Grand Prix",
        "Japanese Grand Prix"
    ]

    def __init__(self, number):
        self.number = number
        self.events_per_race = 10
        self.name = random.choice(self.RACE_NAMES)
        self.RACE_NAMES.remove(self.name)

#Driver class
class Driver:
    def __init__(self):
        self.level = 1

    def upgrade(self):
        if self.level < 4:
            self.level += 1

# Car class
class Player_car:
    def __init__(self):
        self.level = 1

    def upgrade(self):
        if self.level < 4:
            self.level += 1

# Opponent car class
class Opponent_car:
    def __init__(self):
        self.level = random.randint(1, 4)

# Race
class Race:
    def __init__(self):
# Events
    self.events = ['Race start', 'Straight battle', 'High-speed corner battle', 'Medium-speed corner battle',
                    'Low-speed corner battle', 'Crash', 'Pit stop', 'Race finish']
# Race start
    def race_start(self):
        if random.random() < 0.9:  
            print("Race start successful!")
            return True
        else:
            print("DNF. You crashed with another driver and are out of this race")
            return False

# Straight battle
    def straight_battle(self, player_driver, player_car, opponent_car):
        if player_driver.level >= 3 and player_car.level == opponent_car.level:
            print("Straight line overtake successful!")
            return player_car
        elif player_car.level > opponent_car.level:
            print("Straight line overtake failed.")
            return player_car
        elif player_car.level == opponent_car.level:
            print("Straight line overtake failed.")
            return opponent_car
        else:
            print("Overtake failed.")
            return opponent_car

# Low speed corner battle
    def low_speed_corner_battle(self, player_driver, opponent_driver):
        if player_driver.level > opponent_driver.level:
            print("Low-speed corner overtake successful!")
            return "Player's car"
        elif player_driver.level == opponent_driver.level:
            print("Low-speed corner overtake failed.")
            return None
        else:
            print("Low-speed corner overtake failed")
            return "Opponent's car"










    def run_race(self):
        print("Race started!")
        if random.choices([True, False], weights=[9, 1])[0]:  # Weighted choice for successful race start
            print("Race start successful!")
            for event in range(10):  # 10 events after the successful start
                print(f"Event {event+1}: {random.choice(self.events)}")
            print("Race finish!")  # Race finish after 10 random events
        else:
            print("DNF. You crashed.")
            print("Race finish! Position is last place.\n")  # If the race starts with a crash, it finishes immediately








        print(f"Event 1: {self.events[0]}")  # Race start
        for event in range(1, 11):  # Starting from 1 to skip race start
            print(f"Event {event+1}: {random.choice(self.events[1:-1])}")  # Excluding race start and finish
        print(f"Event 12: {self.events[-1]}")  # Race finish
        print("Race finished!\n")

# Race start
        








class Championship:
race_names = ["British Grand Prix", "Italian Grand Prix", "Monaco Grand Prix", "Brazilian Grand Prix", "Belgian Grand Prix"]
    def __init__(self, race_names, num_events_per_race=10, max_events=50):
        self.race_names = race_names
        self.num_events_per_race = num_events_per_race
        self.max_events = max_events
        self.current_race_number = 0
        self.current_event_number = 0

    def start_race(self):
        while self.current_race_number < len(self.race_names):
            self.current_race_number += 1
            print(f"Starting Race: {self.current_race_number} - {self.race_names[self.current_race_number - 1]}")
            while self.current_event_number < self.max_events:
                self.current_event_number += 1
                print(f"Event {self.current_event_number} in progress for {self.race_names[self.current_race_number - 1]}...")
                if self.current_event_number % self.num_events_per_race == 0:
                    self.end_race()
        print("All races completed!")

# Menu to upgrade after race
def upgrade_menu(self):
        print("\nUpgrade Menu:")
        print("1. Upgrade Driver Level")
        print("2. Upgrade Car Level")
        print("3. Upgrade Engineer Level")
        print("4. Upgrade Pit Crew Level")
        print("5. Continue to Next Race")
        choice = input("Enter your choice: ")
        if choice == "1":
            self.upgrade_driver()
        elif choice == "2":
            self.upgrade_car()
        elif choice == "3":
            self.upgrade_engineer()
        elif choice == "4":
            self.upgrade_pit_crew()
        elif choice == "5":
            pass  # Continue to the next race
        else:
            print("Invalid choice. Please choose again.")
            self.upgrade_menu()

    def upgrade_driver(self):
        self.driver_level += 1
        print(f"Driver Level Upgraded to Level {self.driver_level}!")

    def upgrade_car(self):
        self.car_level += 1
        print(f"Car Level Upgraded to Level {self.car_level}!")

    def upgrade_engineer(self):
        self.engineer_level += 1
        print(f"Engineer Level Upgraded to Level {self.engineer_level}!")

    def upgrade_pit_crew(self):
        self.pit_crew_level += 1
        print(f"Pit Crew Level Upgraded to Level {self.pit_crew_level}!")


# Randomizer for events during a race
def trigger_random_event(self):
        events = ["Straight battle", "High-speed corner battle", "Medium-speed corner battle", "Low-speed corner battle", "Crash", "Pitstop"]
        event = random.choice(events)
        print(f"- {event}!")












# Add a pit crew member
def add_pit_crew_members(num_additional_crew_members):
        self.pit_crew_members.append(pit_crew_member)
    
    def calculate_pit_stop_time(num_pit_crew_members):
    # Lookup table for average pit stop times in seconds to the tenth value
    pit_stop_times = {
        2: 45,
        3: 30,
        6: 20,
        10: 7.5,
        14: 3.5,
        16: 2.5,
        20: 1.8,
    }
    



# Add an engineer
def add_engineer(num_additional_engineers):
        self.engineers.append(engineer)



    
    
    def add_location(self, location: Location):
        """Add a location to the game."""
        self.locations.append(location)

    def add_event(self, event: Event):
        """Add an event to the game."""
        self.events.append(event)

    

    def start_game(self):
        return self._main_game_loop()

    def _main_game_loop(self):
        """The main game loop."""
        while self.continue_playing:
            pass
            # ask for user input
            # parse user input
            # update game state
            # check if party is all dead
            # if part is dead, award legacy points and end instance of game
            # if party is not dead, continue game
        if self.continue_playing is False:
            return True
        elif self.continue_playing == "Save and quit":
            return "Save and quit"
        else:
            return False








