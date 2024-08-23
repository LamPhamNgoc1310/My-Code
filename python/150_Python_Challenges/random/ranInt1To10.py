import random
num = random.randint(1,10)
user = int(input("Enter a number: "))
while user != num:
    if user < num:
        print("Higher")
    elif user > num:
        print("Lower")
    user = int(input("Enter a number: "))
print("Woohoo!")