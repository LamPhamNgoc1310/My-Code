import random
num = random.randint(1,5)
for i in range(2):
    user = int(input("Enter a number:"))
    if user == num:
        print("Correct")
        break
    else:
        print("NO!")

    