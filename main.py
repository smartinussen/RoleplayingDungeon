import random

player_health = 100
monster_health = 150
print("\033c\033[3J")
print(f'''
### ##   ##  ###  ###  ##   ## ##   ### ###   ## ##   ###  ##  
 ##  ##  ##   ##    ## ##  ##   ##   ##  ##  ##   ##    ## ##  
 ##  ##  ##   ##   # ## #  ##        ##      ##   ##   # ## #  
 ##  ##  ##   ##   ## ##   ##  ###   ## ##   ##   ##   ## ##   
 ##  ##  ##   ##   ##  ##  ##   ##   ##      ##   ##   ##  ##  
 ##  ##  ##   ##   ##  ##  ##   ##   ##  ##  ##   ##   ##  ##  
### ##    ## ##   ###  ##   ## ##   ### ###   ## ##   ###  ##  G A M E
----------------------------------------------------------------------
''')
player_name = input("What is your name brave warrior: ")
print("\033c\033[3J")
print(f'''
#################################################################################
   Hi {player_name}. Welcome to the Monster and Dungeon turn-based game.       
                                                                              
   You have entered a dungeon and encountered a monster. It looks mad as hell  
   Now, you have 3 choices: (A)ttack, (H)eal or (R)un away                     
                                                                             
#################################################################################
''')
while True:
    try:
        user_action = input("What is your choice of action (a, h or r) ?")
        if user_action.lower() == 'a':
            add_damage = random.randint(10, 15)
            if add_damage % 3 == 0:
                print("WOW! Critical hit ⚔️")
                monster_health -= add_damage*3
            else:
                monster_health -= add_damage
            if monster_health <= 0:
                print("Hooray, the monster is slayed ")
                break
            else:
                print(f"The monster is weakened by {add_damage} HP")
        elif user_action.lower() == 'h':
            player_health += 30
            if player_health > 100:
                print("Your health is at max 💪🏻")
                player_health = 100
        elif user_action.lower() == 'r':
            print("\033c\033[3J")
            print("You ran away you coward! 🏃🏼")
            break
        else:
            print("\033c\033[3J")
            print("Wrong input. Try again with a, h or r")
            continue
        if monster_health > 0:
            monster_damage = random.randint(15, 20)
            player_health -= monster_damage
            print("The monster attacks you. 😵Ouch!\n")
            if player_health <= 0:
                print("\033c\033[3J")
                print('''
                 _      _                        _               _        .___  _ .___  /
                  `.   /    __.  ,   .        ___/ `   ___    ___/        /   \ | /   \ |
                    `./   .'   \ |   |       /   | | .'   `  /   |        |__-' | |,_-' |
                    ,'    |    | |   |      ,'   | | |----' ,'   |        |  \  | |     |
                 _-'       `._.' `._/|      `___,' / `.___, `___,' /      /   \ / /     `
                                                 `               `                      '
                ''')
                break
            else:
                print(f"He dealt you a stroke worth {monster_damage} HP\n")
    except KeyboardInterrupt:
        print(" Nuh-uuh. You cannot escape (unless you run away)")
