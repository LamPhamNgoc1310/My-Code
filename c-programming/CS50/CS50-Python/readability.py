str = input("Please put in a wall of text:")

l = 0
s = 0

for i in range(len(str)):
    # print(str[i])
    if str[i] != " ":
        l += 1
    if str[i] == "!" or str[i] == "." or str[i] == '?':
        s += 1

print("Your grade is: ", end = '')
print(0.0588 * l - 0.296 * s - 15.8)



