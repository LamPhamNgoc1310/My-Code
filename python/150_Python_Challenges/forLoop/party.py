number = int(input("Number of people: "))
if number < 10:
    for i in range(1, number+1):
        name = input(f"Name {i}: ")
        print(f"{name} is invited")
else:
    print("Too many people")