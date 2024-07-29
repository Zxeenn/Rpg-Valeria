import os
import time
import random

# Define Items with Rarities
ITEMS = {
    "potion": {"name": "Potion", "rarity": 0.5},
    "bronze-sword": {"name": "Bronze Sword", "rarity": 0.3, "Damage": 4},
    "scroll": {"name": "Scroll", "rarity": 0.15},
    "steel_dagger": {"name": "Steel Dagger", "rarity": 0.05, "Damage": 7},
    "iron_sword": {"name": "Iron Sword", "rarity": 0.2, "Damage": 5},
    "silver_sword": {"name": "Silver Sword", "rarity": 0.1, "Damage": 6},
    "leather_armor": {"name": "Leather Armor", "rarity": 0.25, "Defense": 2},
    "chain_mail": {"name": "Chain Mail", "rarity": 0.15, "Defense": 3},
    "plate_mail": {"name": "Plate Mail", "rarity": 0.1, "Defense": 4}
}

# Define Enemies with Properties
ENEMIES = {
    "goblin": {"name": "Goblin", "health": 20, "attack": 5},
    "orc": {"name": "Orc", "health": 40, "attack": 10},
    "dragon": {"name": "Dragon", "health": 100, "attack": 25}
}

# Inventory management
inventory = {}

def add_to_inventory(inventory, item_name, quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity

# Display inventorty function shows inventory once called
def display_inventory(inventory):
    inventory_str = "Inventory:\n"
    for item, quantity in inventory.items():
        inventory_str += f" - {ITEMS[item]['name']}: {quantity}\n"
    return inventory_str

# Defines player stats and gear

Level = 1
XP = 0
XP_Max = 20 * Level * Level / 9

item_name = None

def player(XP, XP_Max, Level, item_name):
    # XP and Level up system
    if XP >= XP_Max:
        while XP >= XP_Max:
            XP -= XP_Max
            Level += 1
            XP_Max = 20 * Level * Level / 9

            
    Health = int(10 * Level + Level / 2)
    Strength = 10
    Damage = int(Strength / 3 + 1)
    if item_name in ITEMS:
        Damage += ITEMS[item_name]["Damage"]
    Speed = 0
    Defense = 0
    Magic = 0
    Luck = 0
    Crit = 0
    Crit_DMG = 1
    Dodge = 0
    
    Equipped_Weapon = None
    Equipped_Armor = None
    
    return {"Level": Level, "Health": Health, "Strength": Strength, "Damage": Damage,
            "Speed": Speed, "Defense": Defense, "Magic": Magic, "Luck": Luck,
            "Crit": Crit, "Crit_DMG": Crit_DMG, "Dodge": Dodge, "Inventory": inventory,
            "Equipped_Weapon": Equipped_Weapon, "Equipped_Armor": Equipped_Armor}

# Displays player stats and equips
def display_player_stats(stats):
    stats_str = (
        # Stats UI
        f"Level: {stats['Level']}\n"
        f"Health: {stats['Health']}\n"
        f"Strength: {stats['Strength']}\n"
        f"Damage: {stats['Damage']}\n"
        f"Speed: {stats['Speed']}\n"
        f"Defense: {stats['Defense']}\n"
        f"Magic: {stats['Magic']}\n"
        f"Luck: {stats['Luck']}\n"
        f"Crit: {stats['Crit']}\n"
        f"Crit DMG: {stats['Crit_DMG']}\n"
        f"Dodge: {stats['Dodge']}\n"

        # Equipped items UI
        f"Equipped Weapon: {stats['Equipped_Weapon'] if stats['Equipped_Weapon'] else 'None'}\n"
        f"Equipped Armor: {stats['Equipped_Armor'] if stats['Equipped_Armor'] else 'None'}"
    )
    return stats_str

# Title Screen
def title_screen():
    player_stats = player(XP, XP_Max, Level, item_name)  # Make sure to initialize player stats
    
    print("####################")
    print("# Welcome to Valeria!")
    print("# Play:(1)")
    print("# Options:(2)")
    print("# Equip:(3)")
    print("# About:(4)")
    print("# Credits:(5)")
    print("# Exit:(6)")
    
    TS_Input = ""
    
    while TS_Input not in ["1", "2", "3", "4", "5", "6"]:
        
        TS_Input = input("\n:")
        
        if TS_Input == "1":
            
            os.system('clear')
            
            print("Loading...")
            
            time.sleep(0.5)
            
            os.system('clear')
            
            level_design(player_stats)
            
        elif TS_Input == "2":
            
            os.system('clear')
            
            print("Loading...")
            
            time.sleep(0.5)
            
            os.system('clear')
            
            print("Options:")
            print("Empty Floor Pattern:(1)")
            
        elif TS_Input == "3":
            
            os.system('clear')
            
            print("Loading...")
            
            time.sleep(0.5)
            
            os.system('clear')

            player_stats = player(XP, XP_Max, Level, item_name)
            equip_ui(player_stats)
            
        elif TS_Input == "4":
            
            os.system('clear')
            
            print("Loading...")
            
            time.sleep(0.5)
            
            os.system('clear')
            
            print('Valeria is a text-based adventure game.')
            print('Made using Python')
            print('Made on July 25, 2024')
            
        elif TS_Input == "5":
            print("This game was made by: Kyler Ornelas")
            
        elif TS_Input == "6":
            print("Exiting...")
            exit()

def level_design(player_stats):
    Floor = '·'  # Floor tile
    Wall = '◼'   # Represents walls
    Door = 'D'   # Represents door
    Item = 'I'   # Represents an item on the floor
    Enemy = 'E'  # Represent enemies
    Width = 20   # Map Width
    Height = 20  # Map Height
    Num_Items = random.randint(10, 50)  # Number of items to spawn
    Num_Enemies = random.randint(4, 10)  # Number of enemies to spawn

    # Draws screen full of dots (Width x Height)
    screen = [[Floor for _ in range(Width)] for _ in range(Height)]

    # Draws walls on the edges of the map
    for i in range(Width):
        screen[0][i] = Wall
        screen[Height - 1][i] = Wall
    for i in range(Height):
        screen[i][0] = Wall
        screen[i][Width - 1] = Wall

    # Draws doors on a random side and spot on the map
    door_place = random.randint(1, Width - 2)
    door_side = random.randint(1, 4)
    door_cords = None

    if door_side == 1:
        screen[0][door_place] = Door
        door_cords = (0, door_place)
    elif door_side == 2:
        screen[door_place][0] = Door
        door_cords = (door_place, 0)
    elif door_side == 3:
        screen[Height - 1][door_place] = Door
        door_cords = (Height - 1, door_place)
    elif door_side == 4:
        screen[door_place][Width - 1] = Door
        door_cords = (door_place, Width - 1)

    # Draws initial player location
    Player_Cords = (10, 10)
    screen[10][10] = 'P'

    # Add random items to the level
    item_positions = []
    item_keys = list(ITEMS.keys())
    
    while len(item_positions) < Num_Items:
        
        x = random.randint(1, Height - 2)
        y = random.randint(1, Width - 2)
        
        if screen[x][y] == Floor:
            
            item_name = random.choices(item_keys, weights=[ITEMS[key]['rarity'] for key in item_keys])[0]
            screen[x][y] = Item
            item_positions.append((x, y, item_name))

    # Add random enemies to the level
    enemy_positions = []
    enemy_keys = list(ENEMIES.keys())
    
    while len(enemy_positions) < Num_Enemies:
        
        x = random.randint(1, Height - 2)
        y = random.randint(1, Width - 2)
        
        if screen[x][y] == Floor:
            
            enemy_name = random.choices(enemy_keys, k=1)[0]
            screen[x][y] = Enemy
            enemy_positions.append((x, y, enemy_name))

    # Hardcoded (map #1)
    screen[3][5] = Wall
    screen[5][8] = Wall
    screen[8][10] = Wall
    screen[11][17] = Wall
    screen[14][15] = Wall
    screen[15][15] = Wall
    screen[14][10] = Wall
    screen[16][6] = Wall
    screen[15][6] = Wall
    screen[4][15] = Wall

    for i in range(7):
        screen[2][i + 2] = Wall
        screen[4][i + 2] = Wall
        screen[i+9][8] = Wall
        screen[2][i+11] = Wall
        screen[i+3][17] = Wall
        screen[17][i+6] = Wall
        screen[15][4] = Wall
        
    for i in range(5):
        screen[6][i + 2] = Wall
        screen[i + 7][6] = Wall
        screen[7][i + 7] = Wall
        screen[i + 2][10] = Wall
        screen[i+10][4] = Wall
        screen[i+9][12] = Wall
        screen[i+5][13] = Wall
        screen[i+6][15] = Wall
        screen[i+12][17] = Wall
        screen[15][i+10] = Wall
        screen[i+13][2] = Wall
        
    for i in range(3):
        screen[i + 8][2] = Wall
        screen[8][i + 3] = Wall
        screen[13][i+5] = Wall
        screen[12][i+9] = Wall
        screen[4][i+12] = Wall
        screen[11][i+14] = Wall
        screen[17][i+15] = Wall
        screen[13][i+13] = Wall
        screen[17][i+3] = Wall
    
    # Initialize player and inventory
    inventory = player_stats['Inventory']

    # Notification queue
    notifications = []

    # Display map and handle player movement
    while Player_Cords != door_cords:
        
        os.system('clear')
        
        # Display map with stats and inventory
        map_width = Width
        
        sidebar_width = 40  # Increased width for additional UI components

        # Generate map lines
        map_lines = [" ".join(screen[i]) for i in range(Height)]

        # Prepare inventory, player stats, and equip UI display
        inventory_str = display_inventory(inventory)
        
        stats_str = display_player_stats(player_stats)

        # Calculate sidebar width based on the length of inventory and stats
        sidebar_lines = (inventory_str + "\n" + stats_str).splitlines()

        # Ensure sidebar lines have consistent width
        sidebar_lines = [line.ljust(sidebar_width) for line in sidebar_lines]

        # Print map and sidebar side-by-side
        for i in range(Height):
            map_line = map_lines[i]
            # Ensure that we don't try to access out-of-range sidebar lines
            sidebar_line = sidebar_lines[i] if i < len(sidebar_lines) else " " * sidebar_width
            # Print map line and corresponding sidebar line
            print(map_line + " " * (sidebar_width - len(map_line)) + sidebar_line)

        # Print notifications
        for notification in notifications:
            print(notification)
        notifications = []  # Clear notifications after displaying

        # Player movement or equip input
        move = input("Move (w/a/s/d) or Equip (e): ").lower()
        if move == 'e':
            
            equip_ui(player_stats)  # Open equip menu
            
            continue  # Skip the rest of the loop to re-display the map
            
        else:
            
            new_cords = move_player(Player_Cords, move)

            if is_valid_move(new_cords, screen):
                
                if screen[new_cords[0]][new_cords[1]] == Item:
                    
                    item_name = next(name for (x, y, name) in item_positions if (x, y) == new_cords)
                    
                    add_to_inventory(inventory, item_name, 1)
                    
                    item_positions = [(x, y, name) for (x, y, name) in item_positions if not (x == new_cords[0] and y == new_cords[1])]
                    
                    screen[new_cords[0]][new_cords[1]] = Floor
                    
                    notifications.append(f"Found a {ITEMS[item_name]['name']}!")

                elif screen[new_cords[0]][new_cords[1]] == Enemy:
                    
                    enemy_name = next(name for (x, y, name) in enemy_positions if (x, y) == new_cords)
                    enemy = ENEMIES[enemy_name]
                    
                    notifications.append(f"Encountered a {enemy['name']}! Health: {enemy['health']}, Attack: {enemy['attack']}")

                elif screen[new_cords[0]][new_cords[1]] == Door:
                    
                    print("Congratulations! You reached the door.")
                    print(display_inventory(player_stats['Inventory']))
                    return

                screen[Player_Cords[0]][Player_Cords[1]] = Floor
                
                Player_Cords = new_cords
                
                screen[Player_Cords[0]][Player_Cords[1]] = 'P'
                
            else:
                print("Invalid move. Try again.")

def move_player(current_cords, direction):
    
    if direction == 'a':
        return (current_cords[0], current_cords[1] - 1)
        
    elif direction == 'd':
        return (current_cords[0], current_cords[1] + 1)
        
    elif direction == 'w':
        return (current_cords[0] - 1, current_cords[1])
        
    elif direction == 's':
        return (current_cords[0] + 1, current_cords[1])
        
    else:
        print("Invalid input. Use 'w', 'a', 's', 'd', or 'e'.")
        return current_cords

def is_valid_move(new_cords, screen):
    
    return (0 <= new_cords[0] < len(screen) and
            0 <= new_cords[1] < len(screen[0]) and
            screen[new_cords[0]][new_cords[1]] != '◼')

# Equipable Items
EQUIPABLE_WEAPONS = ["bronze-sword", "steel_dagger", "iron_sword", "silver_sword"]
EQUIPABLE_ARMOR = ["leather_armor", "chain_mail", "plate_mail"]

def equip_item(player_stats, item_name):
    
    if item_name not in ITEMS:
        return "Item does not exist."

    if item_name in EQUIPABLE_WEAPONS:
        
        if item_name in inventory:
            
          if player_stats.get('Equipped_Weapon'):
              
              return "You are already wielding a weapon."
              
          player_stats['Equipped_Weapon'] = ITEMS[item_name]
          return f"Equipped {ITEMS[item_name]['name']} as your weapon."

    elif item_name in EQUIPABLE_ARMOR:
        
        if item_name in inventory:
            
          if player_stats.get('Equipped_Armor'):
              
              return "You are already wearing armor."
              
        player_stats['Equipped_Armor'] = ITEMS[item_name]
        return f"Wearing {ITEMS[item_name]['name']} as your armor."

    else:
        return "This item cannot be equipped."


def equip_ui(player_stats):
    
    os.system('clear')
    
    print("### Equip Menu ###")
    print("Available Weapons:")
    
    for item in ITEMS:
        
        if item in EQUIPABLE_WEAPONS:
            
            print(f" - {ITEMS[item]['name']}")

    print("Available Armor:")
    
    for item in ITEMS:
        
        if item in EQUIPABLE_ARMOR:
            
            print(f" - {ITEMS[item]['name']}")

    chosen_item = input("Enter the name of the item you want to equip: ").strip().lower()

    item_name = None
    
    for key, value in ITEMS.items():
        
        if value['name'].lower() == chosen_item:
            
            item_name = key
            break

    if item_name:
        
        result = equip_item(player_stats, item_name)
        
        print(result)
        print(display_player_stats(player_stats))
        player(XP, XP_Max, Level, item_name)
        
    else:
        
        print("Item not recognized.")

# Run the game
if __name__ == "__main__":
    
    title_screen()
