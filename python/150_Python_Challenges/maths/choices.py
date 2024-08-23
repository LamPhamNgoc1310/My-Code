print("""1) Square 
2) Triangle""")
      
n = int(input("Enter a number: "))

if n == 1:
    a = float(input("Enter the length of your square: "))
    print("Area: ", a**2 )
elif n == 2:
    a = float(input("Enter the length of the base: "))
    h = float(input("Enter the length of the height : "))
    print("Area: ", a*h*1/2)
