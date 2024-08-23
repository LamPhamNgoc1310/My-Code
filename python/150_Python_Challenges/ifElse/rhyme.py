rhyme = input("Enter a random rhyme: ")
print("Your rhyme's length: ", len(rhyme))

start = int(input("Enter a starting number: "))
end = int(input("Enter an ending number: "))

print(rhyme[start-1:end+1])