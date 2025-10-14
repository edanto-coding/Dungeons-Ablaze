import random
import time
import os
import sys
from colorama import Fore, Style, init
init()

# ---------------------- Helper Functions ----------------------
def color(text, fore_color=Fore.WHITE):
    return f"{fore_color}{text}{Style.RESET_ALL}"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_frame(frame):
    clear()
    for line in frame:
        print("".join(line))
    sys.stdout.flush()

def make_sky(sky_color):
    return [[sky_color for _ in range(WIDTH)] for _ in range(HEIGHT)]

def add_sun(frame, sun_y):
    sun_x = WIDTH // 2 - 1
    if 0 <= sun_y < HEIGHT:
        frame[sun_y][sun_x] = SUN
    return frame

def add_ground(frame):
    for y in range(HEIGHT - 6, HEIGHT):
        for x in range(WIDTH):
            frame[y][x] = GROUND
    return frame

# ---------------------- Animations ----------------------
def sunrise():
    sky_colors = [color("🟦", Fore.BLUE), color("🟩", Fore.LIGHTBLUE_EX),
                  color("🟨", Fore.YELLOW), color("🟧", Fore.RED)]
    for i in range(20):
        frame = make_sky(sky_colors[min(i // 5, len(sky_colors) - 1)])
        frame = add_sun(frame, HEIGHT - 10 - i)
        frame = add_ground(frame)
        print_frame(frame)
        time.sleep(0.2)

def cave_scene():
    for t in range(20):
        frame = make_sky(color("⬛", Fore.BLACK))
        # Cave mouth
        for y in range(HEIGHT - 8, HEIGHT):
            for x in range(WIDTH):
                frame[y][x] = GROUND
        for y in range(12, HEIGHT - 8):
            for x in range(20, 44):
                if (x + y) % 2 == 0:
                    frame[y][x] = CAVE
        # Running characters
        guy_x = 22 + t * 2
        if guy_x < WIDTH - 2:
            frame[HEIGHT - 9][guy_x] = GUY1
        if 0 < guy_x - 4 < WIDTH - 2:
            frame[HEIGHT - 9][guy_x - 4] = GUY2
        print_frame(frame)
        time.sleep(0.15)

def main_animation():
    sunrise()
    time.sleep(1)
    cave_scene()
    print(color("The adventurers escape the cave into the new dawn...", Fore.LIGHTYELLOW_EX))
    time.sleep(2)

# ---------------------- Game Setup ----------------------
generic_loot = [
    "50 gold coins",
    "healing potion (10 HP)",
    "mana potion (10 MP)",
    "small gem",
    "torch",
    "leather armor piece",
    "iron dagger",
    "scroll of minor knowledge",
]

hp = 100
WIDTH, HEIGHT = 64, 32
SUN = "☀️"
SKY = "  "
GROUND = color("🟫", Fore.YELLOW)
CAVE = color("⬛", Fore.BLACK)
GUY1 = color("🧍", Fore.LIGHTWHITE_EX)
GUY2 = color("🧍‍♂️", Fore.LIGHTYELLOW_EX)

# ---------------------- Player Setup ----------------------
speed_choice = int(input("1 for fast text. 2 for medium fast text. 3 for slow text: "))
timebetweenwords = {1: 0.1, 2: 0.5, 3: 1}[speed_choice]

print(color("\nGame concept by Edanto Midas. Thank you for playing.", Fore.MAGENTA))
print("This game requires you to keep track of inventory and non-numerical values on paper.")
time.sleep(timebetweenwords)
print("Things like class are also recorded internally.")
time.sleep(timebetweenwords)

name = input("What may your name be, adventurer? ")
time.sleep(timebetweenwords)
print(f"{name}, what an interesting name.")

# ---------------------- Class Selection ----------------------
class_choice = int(input(
    "Choose your class:\n"
    "1: Runic Knight (vanguard, decayer, manipulator)\n"
    "2: Demon Hunter (ravager, destroyer)\n"
    "3: Mage (frost, flame, electrical)\n"
))

if class_choice == 1:
    pclass = "Runic Knight"
    subclass_choice = int(input("Choose subclass: 1: vanguard, 2: decayer, 3: manipulator, 4: random "))
    if subclass_choice == 1:
        subclass = "vanguard"
        hp = 175
    elif subclass_choice == 2:
        subclass = "decayer"
    elif subclass_choice == 3:
        subclass = "manipulator"
    else:
        rksc = ("vanguard", "decayer", "manipulator")
        subclass = random.choice(rksc)
        if subclass == "vanguard": hp = 175

elif class_choice == 2:
    pclass = "Demon Hunter"
    subclass_choice = int(input("Choose subclass: 1: Ravager, 2: Destroyer, 3: random "))
    if subclass_choice == 1:
        subclass = "Ravager"
        hp = 150
    elif subclass_choice == 2:
        subclass = "Destroyer"
        hp = 150
    else:
        subclass = random.choice(("Ravager", "Destroyer"))
        hp = 150

elif class_choice == 3:
    pclass = "Mage"
    subclass_choice = int(input("Choose subclass: 1: frost, 2: flame, 3: electrical, 4: random "))
    if subclass_choice == 1:
        subclass = "frost"
    elif subclass_choice == 2:
        subclass = "flame"
    elif subclass_choice == 3:
        subclass = "electrical"
    else:
        subclass = random.choice(("frost", "flame", "electrical"))

title = f"{name} the {subclass} {pclass}"
print(f"Welcome {title} to ")
input(color("dungeons ablaze", Fore.YELLOW))
time.sleep(timebetweenwords)
input("Press Enter to continue.")

# ---------------------- Subclass Items ----------------------
subclass_items = {
    "vanguard": "shield of life",
    "decayer": "staff of the decayer king",
    "manipulator": "bostaff of health",
    "Ravager": "scythe of corpses",
    "Destroyer": "destroyers katanas",
    "frost": "staff of frozen life",
    "flame": "staff of burning hell",
    "electrical": "cutlass of shock"
}

subclassitem = subclass_items[subclass]

# ---------------------- Subclass Descriptions ----------------------
if subclass == "vanguard":
    print("You have no spells, Vanguard. Main stat: defense.")
    print(f"{subclassitem}: Every turn you gain +5 health.")
elif subclass == "decayer":
    print("Ah, a Decayer. Spells: burst (10 damage, 10m range, poison bubble), disrupt (0 damage, infinite range, disrupts opponent spells). Main stat: intelligence.")
    print(f"{subclassitem}: Every turn you gain +3 corpses. Can use corpses to heal or deal damage.")
elif subclass == "manipulator":
    print("Ah, a Manipulator. Spells: self heal (10 health, no range), harm (20 damage, infinite range). Main stat: intelligence.")
    print(f"{subclassitem}: Every turn you gain +5 health.")
elif subclass == "Ravager":
    print("Spell: Ravage; destroys the environment for damage. Main stat: attack.")
    print(f"{subclassitem}: Every turn you gain +5 corpses.")
elif subclass == "Destroyer":
    print("No spells. Main stat: attack.")
    print(f"{subclassitem}: Every turn your attack stat doubles for the battle.")
elif subclass == "frost":
    print("Spell: Freeze; 5 damage, 50 DOT 10 sec, 20m range, freezes enemy. Main stat: wisdom.")
    print(f"{subclassitem}: Every turn you gain +5 health and have a permanent frost aura.")
elif subclass == "flame":
    print("Spell: Fireblast; 25 damage, 30 DOT 3 sec, 20m range, burns enemy. Main stat: wisdom.")
    print(f"{subclassitem}: Enemies attacking you get burned. Cold immunity.")
elif subclass == "electrical":
    print("Spell: Shock; 25 electrical damage, 30 DOT 3 sec, 20m range, chains lightning. Main stat: wisdom.")
    print(f"{subclassitem}: You are immune to shock, release electricity every turn paralyzing enemies.")

time.sleep(timebetweenwords)
input(f"Press Enter to start your journey, {title}")

# ---------------------- Prologue & Choices ----------------------
input(f"PROLOGUE.\n???: DO YOU HAVE IT?\n???: YES DARIUS, I HAVE IT.\nDarius: Good. {name}, you good back there?\n{name}: Yes Darius, I'm fine.\nDarius: Seriously, you're a {subclass}, I thought you'd have gone for anything else.\n{name}: It's really powerful.\nDarius: Yeah, yeah, delusion.")
input(f"{name}: Micheal, how long till we're out?\nMicheal: IDK, THERE'S A FORK! You pick!\nDarius: Be fast, they're gaining on us.")

choice1 = int(input("You see three paths.\n1: Right into swinging axes.\n2: Left into arrows.\n3: Middle dead end with places to hide: "))

if choice1 == 1:
    input(f"You go right. Dodging axes and arrows.\nShopkeeper: Want to buy something? Health potion 5 gold, spell scroll 25 gold (Siphon usable by Vanguard, Decayer, Destroyer).\nMicheal: {name} is {subclass}. If you don't want it, I am.")
    input("Next room: chests for each of you. Micheal suddenly has a heart attack and dies.")
    print(random.choice(generic_loot))
    print(random.choice(generic_loot))
    print(random.choice(generic_loot))
    print(random.choice(generic_loot))
    print(random.choice(generic_loot))
elif choice1 == 2:
    input("You go left. Micheal gets hit by an arrow. You take the artifact. Rip brother.")
    choice2 = int(input("Next fork:\n1: Chest room left.\n2: Hallway to vendor right: "))
    if choice2 == 1:
        input("Chest falls on you. You died.")
        print(color(f"YOU DIED. {title}", Fore.RED))
        quit()
elif choice1 == 3:
    input("Middle path: all three are shot by snipers. You died.")
    print(color(f"YOU DIED. {title}", Fore.RED))
    quit()

input(f"{name}: I see the exit.\nDarius: I do too.\nYou exit with your loot and the {subclassitem}.")

# ---------------------- Animations ----------------------
main_animation()

# ---------------------- Epilogue ----------------------
print(color("1 year later", Fore.MAGENTA))
input(f"Darius: So {name}, I need a favor.\n{name}: What?\nDarius: Bail me out.\nLater, you bail Darius out.\n{name}: Was it from last year?\nDarius: They took the {subclassitem}.\n{name}: They have it.")
input(color("dungeons ablaze", Fore.RED))
print(color("Game by Edanto Midas / Samuel Waalkens. Demo over.", Fore.RED))
input()
