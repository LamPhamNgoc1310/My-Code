a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
sum = a + b
answer = input("Do you still want to continue? (y/n): ")
while (answer == "y"):
    n = int(input("Enter another number please: "))
    sum = sum + n
    answer = input("Do you still want to continue? (y/n): ")
print(sum)