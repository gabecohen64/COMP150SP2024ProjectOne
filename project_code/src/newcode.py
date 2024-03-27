import random

from project_code.src.Statistic import Driver


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
