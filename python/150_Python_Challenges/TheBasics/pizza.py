slices = int(input("How many slices of pizza do you have right now? "))
ate =int(input("How many slices of pizza have you eaten? "))
while slices - ate < 0:
    slices = int(input("How many slices of pizza do you have right now? "))
    ate =int(input("How many slices of pizza have you eaten? "))
print("The number of slices remaining: ", slices - ate)
