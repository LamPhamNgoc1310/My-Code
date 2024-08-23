import random
colours = random.choice(["green", "red", "yellow", "blue", "grey", "your mom"])
count = 0
tryagain = True
# computer = random.choice(colours)
# while colours != user:
while tryagain == True:
    if count == 2:
        print(f"Hey, it could be {colours}")
    user = input("There are 5 colours, pick one\n")
    user = user.lower() 
    if user == colours:
        print(f"YES, you are correct, it's {colours}")
        tryagain = False
    else:   
        if user == "green":
            print("You must be GREEN with envy.")
            count += 1
        elif user == "red":
            print("Your face must be RED right now.")
            count += 1
        elif user == "yellow":
            print("Oof, you almost catch up but encounter a YELLOW light.")
            count += 1
        elif user == "blue":
            print("You must be feeling BLUE right now.")
            count += 1
        elif user == "grey":
            print("Dont you think your guess is a bit GREY?")
            count += 1
        elif user == "your mom":
            print("joe mama can cover the whole rgb strip")
            count += 1
        else:
            print("It's not in there.")
            count += 1

# print(f"YES, you are correct, it's {colours}")