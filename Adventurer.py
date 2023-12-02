
class Adventurer:
    def __init__(self, Name, Race, Level, Mana, Strength, Dexterity, Intelligence, Charisma, AttackPower, Defence, Health, Gold) -> None:

        self.Gold = Gold
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
        target.update_Mana(-5)
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
    
    def buy_potion(self):
        if self.Gold >= 10:
            print(f"You bought a healing potion for 10 gold.")
            self.Gold -= 10
            self.update_Health(20)
        else:
            print("You don't have enough gold to buy a healing potion.")

    def buy_artifact(self):
        if self.Gold >= 50:
            print(f"You bought an artifact to increase your Attack Power for 50 gold.")
            self.Gold -= 50
            self.update_AttackPower(10)
        else:
            print("You don't have enough gold to buy an artifact.")

    def visit_shop(self):
        print("\n----- Welcome to the Shop -----")
        print("1. Buy Healing Potion (10 gold)")
        print("2. Buy Artifact (50 gold)")
        print("3. Leave Shop")
        choice = int(input("Choose your action (1, 2, or 3): "))

        if choice == 1:
            self.buy_potion()
        elif choice == 2:
            self.buy_artifact()
        elif choice == 3:
            print("Leaving the shop.")

class Human(Adventurer):
    def __init__(self, Name) -> None:
        super().__init__(Name, "Human", 1, 20, 20, 20, 20, 20, 10, 0, 100,1000)

class Elf(Adventurer):
    def __init__(self, Name) -> None:
        super().__init__(Name, "Elf", 1, 50, 10, 40, 20, 40, 10, 0, 200,500)

class Dwarf(Adventurer):
    def __init__(self, Name) -> None:
        super().__init__(Name, "Dwarf", 1, 10, 50, 10, 50, 10, 10, 0, 100,2000)
