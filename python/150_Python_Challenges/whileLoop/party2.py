name = input("Enter a name: ")
count = 1
answer = input("Do you want to invite another person? (y/n): ")
while answer == "y": 
    count += 1
    name = input("Enter a name: ")
    answer = input("Do you want to invite another person? (y/n): ")
print(f"{count} people have been invited to the party.")

