pi = 3.14
def cylinder(r, depth):
    a = pi * r**2
    volume = a * depth
    return volume
r = float(input("Enter the radius of the cylinder: "))
depth = float(input("Enter the depth of the cylinder: "))

print(round(cylinder(r, depth), 2))

