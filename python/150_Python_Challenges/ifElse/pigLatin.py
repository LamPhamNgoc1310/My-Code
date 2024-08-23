string = input("Enter a word: ")
vowel = ["a","i", "u", "e", "o"]
if string[0] in vowel:
    string = string[1:] + string[0] + "ay"

else: 
    string = string + "way"
print(string)