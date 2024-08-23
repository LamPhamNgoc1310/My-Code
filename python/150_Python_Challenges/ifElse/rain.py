weather = input("Is it raining?")
if weather.lower() == "yes":
    windy = input("Is it windy?")
    
    if windy.lower() == "yes":
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")