import random
from typing import List

from project_code.src.Character import Character
from project_code.src.Event import Event
from project_code.src.Location import Location
from project_code.src.Statistic import Driver, OpponentCar
class Game:
    def __init__(self):
        self.race = Race()
        self.player = Character("Player")
        self.opponent = Character("Opponent")
        self.location = Location()
        self.round_number = 0
        self.game_running = False

    def start_game(self):
        self.game_running = True
        self.round_number = 1
        while self.game_running:
            print(f"Round {self.round_number}")
            event = self.location.get_event()
            self.handle_event(event)
            self.round_number += 1
        print("Game over.")

    def handle_event(self, event):
        if event == "Race start":
            self.race_start()
        elif event in ['Straight battle', 'High speed corner battle', 'Medium speed corner battle', 'Low speed corner battle']:
            self.battle(event)
        elif event == 'Pit stop':
            self.pit_stop()

    def race_start(self):
        print("Starting the race!")
        if self.race.race_start():
            print("Race started successfully!")
            # Perform any additional actions related to race start

    def battle(self, event):
        print(f"A {event} event occurred!")
        # Get corresponding method from Race class based on the event type
        event_method = getattr(self.race, event.lower().replace(" ", "_"))
        result = event_method(self, self.player.driver, self.player.car, self.player.pit_crew)
        if result == "DNF":
            self.game_running = False  # End the game if the player DNFs
            print("You crashed and are out of the race!")

    def pit_stop(self):
        print("Entering pit stop.")
        # Perform pit stop logic
        # Example: check if the player needs a pit stop, execute the pit stop, update game state, etc.