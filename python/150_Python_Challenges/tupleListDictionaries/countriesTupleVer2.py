countries_tuple = ("vietnam","america","england","australia","canada")
print("The countries in the tuple: ")

for i in range(len(countries_tuple)):
    print(countries_tuple[i])

userSelect = int(input("Please select a number: "))

print(f"The country in the {userSelect}th position is: {countries_tuple[userSelect]}")

