number = int(input("Number: "))
name = input("Enter your name: ")

if number < 10:
    for i in range(number):
        print(f"{name}")
else:
    for i in range(3):
        print(f"Too high")