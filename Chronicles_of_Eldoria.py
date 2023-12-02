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

def main():
    intro()
    a=str(input("So what is your name young Adventurer - "))
    human.p_status()
    elf.p_status()
    dwarf.p_status()
    race= int(input("what is your race Adventurer, 1)human, 2)elf, 3)dwarf,  - "))
    player=race_selection(race,a)
    
    player.p_status()
    
    return

main()