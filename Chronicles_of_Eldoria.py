from Adventurer import*
from Monsters import*
def intro():
    print('''
    In the mystical land of Eldoria, 
    a realm of magic and mystery, 
    an ancient prophecy foretells of an impending darkness that threatens to engulf the entire world.
    You, a young and aspiring adventurer,
    find yourself drawn into this epic tale as the
    chosen one destined to save Eldoria from impending doom.
    ''')

human=Human("human")
elf=Elf("elf")
dwarf=Dwarf("dwarf")

def race_selection(race,name):
    if race ==1:
        player = Human(str(name))
    elif race ==2:
        player = Elf(str(name))
    elif race ==3:
        player = Dwarf(str(name))
    else:
        race_selection(race,str(name))
    return(player)
import random

def battle(player, monster):
    print(f"A wild {monster.Name} appears!")
    while player.Health > 0 and monster.Health > 0:
        print("\n-------------------")
        print("Player's Turn:")
        print("1. Attack")
        print("2. Defend")
        print("3. Run to shop")
        choice = int(input("Choose your action (1 or 2 or 3): "))

        if choice == 1:
            player.attack(monster)
        elif choice == 2:
            print(f"{player.Name} defends and gains 5 Health!")
            player.update_Health(5)
        elif choice == 3:
            print(f"{player.Name} runs to shop")
            player.update_Health(5)
            print("\n----- Running to the Shop -----")
            player.visit_shop()
            
        if monster.Health <= 0:
            print(f"You defeated the {monster.Name}!")
            break

        print("\nMonster's Turn:")
        monster.attack(player)

        if player.Health <= 0:
            print("You have been defeated. Game Over!")
            break

        player.p_status()
        monster.m_status()

def level_up(player):
    print(f"\nCongratulations, {player.Name}! You've leveled up!")
    player.update_Level(player.Level + 1)
    player.update_Health(20)  
    player.p_status()

def main():
    intro()
    player_name = str(input("So what is your name, young Adventurer? - "))
    
    human.p_status()
    elf.p_status()
    dwarf.p_status()
    
    race = int(input("What is your race, Adventurer? 1) Human, 2) Elf, 3) Dwarf - "))
    player = race_selection(race, player_name)
    
    player.p_status()
    

    monster_levels = [Slime("Slime"), Goblin("Goblin"), Orc("Orc"), Undead("Undead"), Werewolf("Werewolf"), Vampire("Vampire")]

    for level, monster in enumerate(monster_levels, start=1):
        print(f"\n----- Level {level} -----")
        battle(player, monster)

        if player.Health > 0: 
            player.p_status()
            s=input("\nWould you like to visit shop- 1)yes, 2)No")
            if s==1:
                print("\n----- Visiting the Shop -----")
                player.visit_shop()
            else:
                pass

    print("\nCongratulations, you have defeated all the monsters and saved Eldoria!")

if __name__ == "__main__":
    main()