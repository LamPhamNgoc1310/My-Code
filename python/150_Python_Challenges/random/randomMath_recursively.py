import random
def randomMath(count,n):
    if n == 5:
        return count
    num1 = random.randint(0,1000)
    num2 = random.randint(0,1000)
    print(f"{num1} + {num2} = ?")
    user = int(input("Enter your result: "))
    res = num1 + num2
    if res == user:
        count += 1
    n += 1
    return randomMath(count,n)

x = randomMath(0,0)
print(f"You get {x} answer(s) correct")


