compnum = 50
guess = int(input("Enter a number:  "))
count = 0
while guess != compnum:
    if guess < compnum:
        print("Higher")
        guess = int(input("Enter a number:  "))
        count += 1
    if guess > compnum:
        print("Lower")
        guess = int(input("Enter a number: "))
        count += 1
print(f"The correct answer is {compnum} and you took {count} attempt(s).")