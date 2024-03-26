import random

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
class Driver:
    def __init__(self):
        self.level = 0  # Assuming level is an attribute of the driver

    def randomize_level(self):
        self.level = random.randint(1, 5)  # Random level between 1 and 5

class OpponentCar:
    def __init__(self):
        self.level = 0  # Assuming level is an attribute of the car

    def randomize_level(self):
        self.level = random.randint(1, 5)  # Random level between 1 and 5

class Strength:
    def __init__(self, value=0):
        self.value = value

    def increase(self, amount):
        self.value += amount

    def decrease(self, amount):
        self.value -= amount

class Constitution:
    def __init__(self, value=0):
        self.value = value

    def increase(self, amount):
        self.value += amount

    def decrease(self, amount):
        self.value -= amount
class Dexterity:
    def __init__(self, value=0):
        self.value = value

    def increase(self, amount):
        self.value += amount

    def decrease(self, amount):
        self.value -= amount
class Vitality:
    def __init__(self, value=0):
        self.value = value

    def increase(self, amount):
        self.value += amount

    def decrease(self, amount):
        self.value -= amount
class Endurance:
    def __init__(self, value=0):
        self.value = value

    def increase(self, amount):
        self.value += amount

    def decrease(self, amount):
        self.value -= amount
class Intelligence:
    def __init__(self, value=0):
        self.value = value

    def increase(self, amount):
        self.value += amount

    def decrease(self, amount):
        self.value -= amount
class Wisdom:
    def __init__(self, value=0):
        self.value = value

    def increase(self, amount):
        self.value += amount

    def decrease(self, amount):
        self.value -= amount
class Knowledge:
    def __init__(self, value=0):
        self.value = value

    def increase(self, amount):
        self.value += amount

    def decrease(self, amount):
        self.value -= amount
class Willpower:
    def __init__(self, value=0):
        self.value = value

    def increase(self, amount):
        self.value += amount

    def decrease(self, amount):
        self.value -= amount
class Spirit:
    def __init__(self, value=0):
        self.value = value

    def increase(self, amount):
        self.value += amount

    def decrease(self, amount):
        self.value -= amount
