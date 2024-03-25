from project_code.src.Statistic import Strength, Dexterity, Constitution, Vitality, Endurance, Intelligence, Wisdom, Knowledge, Willpower, Spirit

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