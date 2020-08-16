from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random as rnd

print("\n\n")


#Damage spells, blak magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 12, 100, "black")
water = Spell("Water", 14, 100, "black")
air = Spell("Air", 16, 100, "black")

#Heal spells, white magic
cure = Spell("Cure", 15, 120, "white")
cura = Spell("Cura", 12, 60, "white")

player_spells = [fire, thunder, water, air, cure, cura]

#Items
potion = Item("Potion", "potion", "Heals 20 HP.", 20)
food = Item("Food", "food", "Heals 50HP", 50)
buffet = Item("Buffet", "buffet", "Heals 100HP", 100)
sleep = Item("Sleep", "sleep", "Complete healing.", 500)
bomb = Item("Bomb", "bomb", "Deals 300 points of damage.", 300)

#player_items = [potion, food, buffet, sleep, bomb]
#si queremos definir cantidad y escribir el nombre del item en vez de poner numero hacemos una lista
player_items = [{"item": potion, "quantity": 15}, {"item": food, "quantity": 15}, {"item": buffet, "quantity": 15},
                {"item": sleep, "quantity": 15}, {"item": bomb, "quantity": 15}]

#People in game
player0 = Person("Pseudoperson", 500, 100, 80, 50, player_spells, player_items)
player1 = Person("The Good", 500, 100, 80, 50, player_spells, player_items)
player2 = Person("The Ugly", 500, 100, 80, 50, player_spells, player_items)
player3 = Person("The Bad", 500, 100, 80, 50, player_spells, player_items)
players = [player1, player2, player3]

enemy = Person("Epic monster", 1000, 50, 150, 30, [], [])

run = True
i = 0
rounds = 1  # Rondas
defeated_players = 0
print("==========================================")

print("The battle has started, starting stats:")
while run:
    print("==========================================")
    print("\n")
    print("ROUND", rounds)
    print("Player name                   HP                                MANA")
    for player in players:
        player.get_stats()
    print("ENEMY                                     HP                       ")
    enemy.get_enemy_stats()

    print("\n")

    for player in players:
  #      print("Good boys attacking")
        player.choose_action()
        choice = input("Choose action:")
        index = int(choice) - 1
    #    if choice == 'quit':
    #        run = False
    #    else:
    #        index = int(choice) - 1
    #        continue

    # ATTACK DAMAGE
        if index == 0:
            dmg = player.gen_damage()
            enemy.take_damage(dmg)
            print(player.name, "attacked", enemy.name, "for", dmg)
        elif index == 1:
            player.choose_spell()
            magic_choice = int(input("Choose spell:")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.gen_damage()
        #        cost = spell.gen_manacost()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print("Not enough mana.")
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(player.name, "chooses",  spell.name + ".", player.name, "heals for", str(magic_dmg))
            elif spell.type == "black":
                enemy.take_damage(magic_dmg)
                print(player.name, "chooses",  spell.name + ".", player.name + "'s", spell, "deals", str(magic_dmg),
                      "points of damage.")

        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print("None left.")
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(item.name + "heals for", str(item.prop))
        # elif item.type == todos los tipos...  añadir un elif para cada item

    enemy_choice = 1

    enemy_dmg = enemy.gen_damage()

    target = rnd.randrange(0, 3 - defeated_players)
    players[target].take_damage(enemy_dmg)
    print("\n")
    print(bcolors.OKRED + str(enemy.name), "attacks", players[target].name, "for", str(enemy_dmg) + bcolors.ENDC)

    print("********************************************************")
    print(" \n STATS AFTER THE BATLLE:")
    print(str(enemy.name), "HP:", str(enemy.get_hp()) + "/" + str(enemy.get_maxhp()))
    for player in players:
        print("-------------------------------------------")
        print(str(player.name), "HP:", str(player.get_hp()) + "/" + str(player.get_maxhp()))
        print(str(player.name), "MANA:", str(player.get_mp()) + "/" + str(player.get_maxmp()))

    if enemy.get_hp() <= 0:
        print("You win!")
        run = False

 #   for player in players:
    if players[target].get_hp() <= 0:
            print(players[target].name, "has been eliminated.")
            defeated_players += 1
            print(defeated_players, "eliminados")
            del(players[target])
    if defeated_players == 2:
        print(enemy.name, "has deafeated you.")
        run = False

    rounds += 1