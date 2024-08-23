countries_tuple = ("vietnam","america","england","australia","canada")
print("The countries in the tuple: ")

for i in range(len(countries_tuple)):
    print(countries_tuple[i])

userSelect = input("Please select a country: ")

print(f"The index of {userSelect} in the list is: {countries_tuple.index(userSelect)+1}")

