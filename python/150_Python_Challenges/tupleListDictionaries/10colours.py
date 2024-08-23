import time

colours = ["red", "green", "blue", 
           "yellow", "orange", "pink",
            "magenta", "purple", "black", "grey"]

user1 = int(input("Enter a starting number between 0 and 4: "))
user2 = int(input("Enter an ending number between 5 and 9: "))

for i in range(user1, user2+1):
    time.sleep(2)
    print(f"{colours[i]}\n")
# alternative
# print(colours[user1:user2+1])
