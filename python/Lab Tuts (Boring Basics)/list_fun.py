import random


print(f"Get ready")

item_ls = ["Donkey", "Boot", "Water bottle", "House"]
color_ls = ["Red", "Yellow", "Blue"]

print(f"{len(item_ls)}")

for i in range(len(item_ls)):
    print(f"index is {i} of {item_ls[i]}")

#Hard to read, good logic, don't need index since pulling choice
for i in range (len(item_ls)):
    x = random.randint(1, ((len(item_ls))-1))
    y = random.randint(1, ((len(color_ls))-1))
    print(f"Random Item is \n {color_ls[y]} {item_ls[x]}")

#better, through away variable '_' and uses random .choice module which is cleaner    
for _ in item_ls:   
    print(f"Random Item is: {random.choice(color_ls)} {random.choice(item_ls)}")
                 