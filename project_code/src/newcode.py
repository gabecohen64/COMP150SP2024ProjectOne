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
