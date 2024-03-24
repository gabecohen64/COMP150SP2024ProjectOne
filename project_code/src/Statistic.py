import random
from tracemalloc import Statistic


# Statistics: pit stop time, lap number, position number, car number, upgrade number, chance of bad pit stop, chance of bad upgrade, chance of crash, chance of pitting under safety car, chance of track event.

class Pit_Stop_Time:
    def __init__(self, seconds: float):
        self.value = self._generate_starting_value(seconds)
        self.description = None
        self.min_value = 0
        self.max_value = 100

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
    
    # Check if the provided number of crew members is within the valid range
    if num_crew_members < 3 or num_crew_members > 22:
        return None  # Return None for invalid input
    
    # Retrieve and return the average pit stop time from the lookup table
    return pit_stop_times[num_crew_members]

# Example usage:
num_crew_members = 10
average_pit_stop_time = calculate_pit_stop_time(num_crew_members)
if average_pit_stop_time is not None:
    print(f"Average pit stop time with {num_crew_members} crew members: {average_pit_stop_time} seconds")
else:
    print("Invalid number of crew members.")
    def __str__(self):
        return f"{self.value}"

    def increase(self, amount):
        self.value += amount
        if self.value > self.max_value:
            self.value = self.max_value

    def decrease(self, amount):
        self.value -= amount
        if self.value < self.min_value:
            self.value = self.min_value

    def _generate_starting_value(self, legacy_points: int):
        """Generate a starting value for the statistic based on random number and user properties."""
        """This is just a placeholder for now. Perhaps some statistics will be based on user properties, and others 
        will be random."""
        return legacy_points % 100 + random.randint(1, 3)


class Strength(Statistic):

    def __init__(self, value):
        super().__init__(value)
        self.description = "Strength is a measure of physical power."

# and so on for the other statistics
