# Author CCG 10/12/21

x1 = input("What is the x coordinate for the first point?")
y1 = input("What is the y coordinate for the first point?")

x2 = input("What is the x coordinate for the second point?")
y2 = input("What is the y coordinate for the second point?")

distance = ((int(x2) - int(x1)) ** 2 + (int(y2) - int(y1)) ** 2) ** 0.5

print("The distance between the two points is " + str(distance))