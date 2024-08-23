number = int(input("Enter a number between 1 and 12: "))
for i in range(1, 13):
    ans = number * i
    print(f"{i} * {number} = {ans}")