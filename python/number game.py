import random

target = random.randint(1,20)
guess = 0
attempts = 0
max_attempts = 2

print("I am thinking of a number between 1 and 20")


while guess != target:
    if attempts >= max_attempts:
        print(f"You failed, you exceeded max attempts of  {max_attempts} the number I was thinking of was {target}")
        exit()
    try:
        guess= int(input("Type in yar number"))
    except ValueError:
        print("Wrong value")
        exit()
    
    attempts = attempts + 1
    if guess > target:
        print("Too high try again")
    elif guess < target:
        print("Too low try again")

print(f"You done it in {attempts} tries ! ")    
    