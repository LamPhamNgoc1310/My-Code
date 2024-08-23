total = 0
for i in range(5):
    number = int(input("Enter a number: "))
    choice = input("Do you want to add this number to the sum? y/n ")
    if choice.lower() == 'y':
        total += number
print(total)
        