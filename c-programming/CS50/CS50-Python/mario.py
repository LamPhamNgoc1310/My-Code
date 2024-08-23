

n = int(input("Please enter a number:"))
for i in range(0,n):
    for j in range(i,n):
        print(" ", end='')
    for k in range(0,i+1):
        print("#", end='')
    print()
