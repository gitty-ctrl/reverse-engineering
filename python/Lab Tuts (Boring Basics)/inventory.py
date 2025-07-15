import random

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))



def addToInventory(inventory, addedItems):
    count = {}
    total_in = {}
    for item in addedItems:
        count.setdefault(item, 0)
        count[item] = count[item]+1
    print(f"Total from Dragon: {count}")
    for key,value in count.items():
        if key not in inventory:
            inventory.setdefault(key,value)
        inventory[key]+= value
    print(f"Total inv {inventory}")
    return inventory
        
def fightTheDragon(answer):
    chance = random.randint(0,10)
    if answer.lower() == "yes" and chance >= 5:
        print(f"You attacked the dragon for {chance * 100} HP Points!")
        print("The dragon died")
        inv = addToInventory(stuff,dragonLoot)
    elif chance == 10:
        print(f"You chopped the dragons head off in one swip!")
        print("The dragon died")
        inv = addToInventory(stuff,dragonLoot)
    else:
        print("You died")
        exit()
    return inv



displayInventory(stuff)
print(f"Get ready to fight the dragon")
answer = input("Will you fight? (Yes/No)")
inv = fightTheDragon(answer)
#inv = addToInventory(stuff, dragonLoot)
#print(inv)
displayInventory(inv)