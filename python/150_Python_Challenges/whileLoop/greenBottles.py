num = int(input("Enter the number of green bottles: "))
while num != 0:
    print(f"""There are {num} green bottles hanging on the wall, 
        {num} green bottles hanging on the wall, 
        and if 1 green bottle should accidentally fall.""")
    num -= 1
    fall = int(input("How many green bottles will be hanging on the wall? "))
    while fall != num:
        fall = int(input("No, try again: "))
    print(f"There are {num} green bottles hanging on the wall")
print("There are no more green bottles hanging on the wall.")
