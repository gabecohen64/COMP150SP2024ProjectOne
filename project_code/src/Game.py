'''game ideas: racing theme, characters are drivers, pit crew members, engineers, and team boss. these characters can receive upgrades. upgraded drivers are faster and more consistent meaning less incidents 
 like spinning out or crashing. upgraded pit crews add more pit crew members per upgrade, meaning faster pit stops. upgraded engineers mean a faster car with upgraded aerodynamics and engine. an upgraded
boss adds more consistency to pit stops and car upgrades. a lower level boss increases the chances of inconsistent pit stop times regardless of the number of members, and it can mean car upgrades may backfire
and make the car slower than before. events could be the race start, pit stops, and battles on sections of track such as straights, high speed, medium speed, and low speed corners. include safety car as cutscene.
safety car is most common pit stop time.'''

from typing import List

from project_code.src.Character import Character
from project_code.src.Event import Event
from project_code.src.Location import Location



class Race:
    def __init__(self):
        self.events = ['Straight battle', 'High speed corner battle', 'Medium speed corner battle',
                       'Low speed corner battle', 'Pit stop']

    def get_race_name(self):
        race_names = ["British Grand Prix", "Italian Grand Prix", "Monaco Grand Prix", "Brazilian Grand Prix", "Belgian Grand Prix"]
        return random.choice(race_names)

    def race_start(self):
        if random.random() < 0.9:  
            print("Race start successful!")
            return True
        else:
            print("DNF. You crashed with another driver and are out of this race.")
            return False

    def straight_battle(self, game, player_driver, player_car, player_pit_crew):
        if random.random() < 0.025:
            print("DNF. You crashed trying a straight line overtake.")
            return "DNF"

        opponent_driver = Driver()
        opponent_car = OpponentCar()
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

    def low_speed_corner_battle(self, game, player_driver, player_car, player_pit_crew):
        if random.random() < 0.05:
            print("DNF. You crashed trying a low speed corner overtake.")
            return "DNF"

        opponent_driver = Driver()
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
