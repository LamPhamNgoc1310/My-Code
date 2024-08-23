import random

count = 0
for i in range(5):
    num1 = random.randint(0,1000)
    num2 = random.randint(0,1000)
    print(f"{num1} + {num2} = ?")
    user = int(input("Enter your result: "))
    res = num1 + num2
    if res == user:
        count += 1
print(f"You got {count} correct")