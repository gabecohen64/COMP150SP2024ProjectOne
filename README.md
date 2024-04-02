# COMP150SP2024ProjectOne

## Team Members
Abdullah I Khan and Gabe Cohen

## Project Description
This is a text-based racing game where you take on the role of a team owner/manager. You get to create your own character with a name, and you have a team consisting of a driver, a pit crew, and an engineer. The game takes you through multiple races at different locations like the British Grand Prix or the Italian Grand Prix. Before each race, you have the option to upgrade your team members (driver, car, or pit crew) to make them better and more competitive. During the race, various events can happen, such as straight battles (overtaking on straights), high/medium/low-speed corner battles (overtaking in corners), and pit stops. The outcome of these events depends on the levels and abilities of your driver, car, and pit crew, as well as your opponent's team. If you perform well in these events, you'll gain points, and if you don't, you'll lose points. The goal is to accumulate enough points to win the championship by the end of all the races. The game has an element of randomness, so even if your team is strong, there's a chance of crashing or failing an overtake attempt. It's a mix of strategy (upgrading your team) and luck (random events during the race).

### The Party
One user playing the game.

### Characters
Driver:
This is the player's driver who participates in the races.
The driver has a level attribute that can be upgraded.
In the Game initialization, a Driver instance with level 4 is created for the player.
Pit Crew:
This represents the player's pit crew team.
The pit crew also has a level attribute that can be upgraded.
In the Game initialization, a Pit_crew instance with level 4 is created for the player.
Engineers:
This is a character class representing the engineering team.
No specific attributes or methods are defined for this class in the provided code.
In the Game initialization, an Engineers instance is created.
Character:
This is a base class for all character types in the game.
It has a name attribute that can be auto-generated or provided during initialization.
In the Game initialization, a Character instance with the name "Team Owner" is created and added to the self.party list.
Opponent Driver:
This is an instance of the Driver class that represents the opponent's driver in the races.
The opponent driver's level is randomized within a specific range during race events.

### Common stats:
Based on the code, the common stats or attributes shared among the different character classes are:

Level:
This attribute is present in the Driver, Pit_crew, and Player_car classes.
It represents the skill or ability level of the driver, pit crew, and the player's car.
The level can be upgraded (up to a certain maximum) using the upgrade method defined in each class.
For the opponent's driver and car, the level is randomized within a specific range using the randomize_level method.
Name:
The Character base class has a name attribute that is either generated automatically or can be provided during initialization.
The Driver and Pit_crew classes inherit from the Character class, so they also have a name attribute.
Stamina (for Driver class only):
The Driver class has an additional stamina attribute, which is initialized to 100.
It's not clear from the provided code how this stamina attribute is used or affected during the game.
Performance (for Player_car and Opponent_car classes):
Both the Player_car and Opponent_car classes have a performance attribute, which is initialized to 100.
During certain race events (e.g., "Straight battle," "High speed corner battle"), the player's car performance is decreased by 1.
The performance attribute seems to be related to the car's ability or effectiveness during the race.

### Events:
Based on the code, the events that can occur during a race in this game are as follows:

Race Start:
This event represents the start of the race.
It is handled by the handle_event method of the Event class.
If the event name is 'Race start', it prints a message indicating that the race has started.
Straight Battle:
This event represents a battle or overtaking attempt on a straight section of the racetrack.
It decreases the player's car performance by 1.
It is handled by the handle_event method of the Event class.
High Speed Corner Battle:
This event represents a battle or overtaking attempt in a high-speed corner section of the racetrack.
It decreases the player's car performance by 1.
It is handled by the handle_event method of the Event class.
Medium Speed Corner Battle:
This event represents a battle or overtaking attempt in a medium-speed corner section of the racetrack.
It decreases the player's car performance by 1.
It is handled by the handle_event method of the Event class.
Low Speed Corner Battle:
This event represents a battle or overtaking attempt in a low-speed corner section of the racetrack.
It decreases the player's car performance by 1.
It is handled by the handle_event method of the Event class.
Pit Stop:
This event represents a pit stop during the race.
It increases the player's car performance by 2. 

### Project Theme: You Decide
Racing theme from F1. 

