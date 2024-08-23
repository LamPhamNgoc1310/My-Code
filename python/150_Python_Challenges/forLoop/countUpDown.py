direct = input("Which direction do you want to count? up/down ")
if direct == "up":
    upper = int(input("Which number do you want to count to? "))
    for i in range(1, upper+1):
        print(f"{i}", end=" ")

elif direct == "down":
    lower = int(input("Enter a number smaller than 20: "))
    if lower < 20:
        for i in range(lower, 0, -1):
            print(f"{i}", end=" ")
