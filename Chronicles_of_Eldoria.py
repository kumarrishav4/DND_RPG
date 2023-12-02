def main():
    return

def intro():
    print('''
    In the mystical land of Eldoria, 
    a realm of magic and mystery, 
    an ancient prophecy foretells of an impending darkness that threatens to engulf the entire world.
    You, a young and aspiring adventurer,
    find yourself drawn into this epic tale as the
    chosen one destined to save Eldoria from impending doom.
    ''')

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

    def p_status(self):
        print(f'''
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

class Monster:
    def __init__(self, Name, Level, Mana, Strength, Dexterity, Intelligence, AttackPower, Defence, Health, Type) -> None:
        self.Name = Name
        self.Level = Level
        self.Mana = Mana
        self.Strength = Strength
        self.Dexterity = Dexterity
        self.Intelligence = Intelligence
        self.AttackPower = AttackPower
        self.Defence = Defence
        self.Health = Health
        self.Type = Type

    def m_status(self):
        print(f'''
                Name--{self.Name}, Race--{self.Type}, Level--{self.Level},
                Mana--{self.Mana}, Strength--{self.Strength}, Dexterity--{self.Dexterity},
                Intelligence--{self.Intelligence}, Attack Power--{self.AttackPower},
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

class Slime(Monster):
    def __init__(self, Name) -> None:
        super().__init__(Name, 1, 0, 1, 1, 2, 1, 0, 10 ,"Slime")

class Goblin(Monster):
    def __init__(self, Name) -> None:
        super().__init__(Name, 2, 0, 10, 5, 5, 10, 10, 20, "Goblin")

class Orc(Monster):
    def __init__(self, Name) -> None:
        super().__init__(Name, 3, 0, 20, 0, 0, 10, 0, 50, "Orc")

class Undead(Monster):
    def __init__(self, Name) -> None:
        super().__init__(Name, 4, 20, 50, 5,0, 10, 20, 100, "Undead")

class Werewolf(Monster):
    def __init__(self, Name) -> None:
        super().__init__(Name, 5, 50, 50, 50, 100, 50, 10, 200, "Werewolf")

class Vampire(Monster):
    def __init__(self, Name) -> None:
        super().__init__(Name, 6, 1000, 500, 500, 100, 500, 1000, 2000,"Vampire")

class Dragon(Monster):
    def __init__(self, Name) -> None:
        super().__init__(Name, 10, 9999, 999, 99, 99, 99, 999, 9999,"Dragon")

class Levels:
    def __init

a = Goblin("gon")
a.m_status()

b = Human("kim")
b.p_status()
