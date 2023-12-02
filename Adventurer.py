
class Adventurer:
    def __init__(self, Name, Race, Level, Mana, Strength, Dexterity, Intelligence, Charisma, AttackPower, Defence, Health) -> None:
        self.Name = Name
        self.Race = Race
        self.Level = Level
        self.Mana = Mana
        self.Strength = Strength
        self.Dexterity = Dexterity
        self.Intelligence = Intelligence
        self.Charisma = Charisma
        self.AttackPower = AttackPower
        self.Defence = Defence
        self.Health = Health
    
    def attack(self, target):
        print(f"{self.Name} attacks {target.Name}!")
        target.update_Mana(-5)  # Decrease target's mana by 5
        target.update_Health(-self.AttackPower)

    def p_status(self):
        print(f'''your current status is
                Name--{self.Name}, Race--{self.Race}, Level--{self.Level},
                Mana--{self.Mana}, Strength--{self.Strength}, Dexterity--{self.Dexterity},
                Intelligence--{self.Intelligence}, Charisma--{self.Charisma}, Attack Power--{self.AttackPower},
                Defence--{self.Defence}, Health--{self.Health}
                ''')
        
    def update_Level(self, newlevel):
        self.Level = newlevel

    def update_Mana(self, new):
        self.Mana += new

    def update_Strength(self, new):
        self.Strength += new

    def update_Dexterity(self, new):
        self.Dexterity += new

    def update_Intelligence(self, new):
        self.Intelligence += new

    def update_AttackPower(self, new):
        self.AttackPower += new

    def update_Defence(self, new):
        self.Defence += new

    def update_Health(self, new):
        self.Health += new

class Human(Adventurer):
    def __init__(self, Name) -> None:
        super().__init__(Name, "Human", 1, 20, 20, 20, 20, 20, 10, 0, 100)

class Elf(Adventurer):
    def __init__(self, Name) -> None:
        super().__init__(Name, "Elf", 1, 50, 10, 40, 20, 40, 10, 0, 200)

class Dwarf(Adventurer):
    def __init__(self, Name) -> None:
        super().__init__(Name, "Dwarf", 1, 10, 50, 10, 50, 10, 10, 0, 100)
