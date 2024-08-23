food = {}
for i in range(4):
    user = input("Please enter the food you like? ")
    food[i] = user

for i in range(len(food)):
    print(food[i], end=" ")

dislike = int(input("\nWhich one do you want to remove? "))

del food[dislike]

for i in range(len(food)):
    print(food[i], end=" ")

# need to find ways to input string instead of int