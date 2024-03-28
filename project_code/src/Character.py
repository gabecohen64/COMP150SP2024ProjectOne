from project_code.src.Statistic import (Strength,
                                        Dexterity,
                                        Constitution,
                                        Vitality,
                                        Endurance,
                                        Intelligence,
                                        Wisdom,
                                        Knowledge,
                                        Willpower,
                                        Spirit)

class Character:
    def __init__(self, name: str = None):
        self.name = self._generate_name() if name is None else name
        self.strength = Strength(self)
        self.dexterity = Dexterity(self)
        self.constitution = Constitution(self)
        self.vitality = Vitality(self)
        self.endurance = Endurance(self)
        self.intelligence = Intelligence(self)
        self.wisdom = Wisdom(self)
        self.knowledge = Knowledge(self)
        self.willpower = Willpower(self)
        self.spirit = Spirit(self)

    def _generate_name(self):
        return "Bob"
    class Race:
        def __init__(self):
            self.events = ['Race start', 'Straight battle', 'High speed corner battle',
                           'Medium speed corner battle', 'Low speed corner battle', 'Pit stop']
def upgrade_driver(self, character):
    character.driver.upgrade()

def upgrade_pit_crew(self, character):
    character.pit_crew.upgrade()

def upgrade_engineer(self, character):
    character.engineer.upgrade()

def upgrade_boss(self, character):
    character.boss.upgrade()

