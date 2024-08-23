larger = int(input("Please enter a number larger than 100: "))
smaller = int(input("Please enter a number smaller than 10: "))

while (smaller > larger or larger <100 or smaller >10):
    larger = int(input("Please enter a number larger than 100: "))
    smaller = int(input("Please enter a number smaller than 10: "))

print(smaller, "goes into",larger, larger//smaller, "times")