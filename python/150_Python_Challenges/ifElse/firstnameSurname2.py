f = input("Enter your first name: ")
s = input("Enter your surname: ")

full = f + s
if len(full) < 5:
    print(full.upper())
else:
    print(full.lower())