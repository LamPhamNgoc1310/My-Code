user = int(input("Please enter a number: "))
# previously used "and" operator and it was logically wrong
while user < 10 or user > 20: 
    if user < 10:
        print("Too low")
        
    elif user > 20:
        print("Too high")
    user = int(input("Please enter a number: "))
print("Thank you for entering number between 10 and 20.")