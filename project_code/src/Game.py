# game ideas: racing theme, characters are drivers, pit crew members, engineers, and boss. these characters can receive upgrades. upgraded drivers are faster and more consistent meaning less incidents 
# like spinning out or crashing. upgraded pit crews add more pit crew members per upgrade, meaning faster pit stops. upgraded engineers mean a faster car with upgraded aerodynamics and engine. an upgraded
# boss adds more consistency to pit stops and car upgrades. a lower level boss increases the chances of inconsistent pit stop times regardless of the number of members, and it can mean car upgrades may backfire
# and make the car slower than before. events could be the race start, pit stops, and battles on sections of track such as straights, high speed, medium speed, and low speed corners. 

from typing import List

from project_code.src.Character import Character
from project_code.src.Event import Event
from project_code.src.Location import Location


class Game:

    def __init__(self):
        self.characters: List[Character] = []
        self.locations: List[Location] = []
        self.events: List[Event] = []
        self.party: List[Character] = []
        self.current_location = None
        self.current_event = None
        self._initialize_game()
        self.continue_playing = True

    def add_character(self, character: Character):
        """Add a character to the game."""
        self.characters.append(character)

    def add_location(self, location: Location):
        """Add a location to the game."""
        self.locations.append(location)

    def add_event(self, event: Event):
        """Add an event to the game."""
        self.events.append(event)

    def _initialize_game(self):
        """Initialize the game with characters, locations, and events based on the user's properties."""
        pass

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








