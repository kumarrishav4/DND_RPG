from Adventurer import*
from Monsters import*

def main_story():
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

a = Goblin("gon")
a.m_status()

b = Human("kim")
b.p_status()
