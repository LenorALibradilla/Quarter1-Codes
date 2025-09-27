import math

x1 = float(input("Enter x1:"))
y1 = float(input("Enter y1:"))
x2 = float(input("Enter x2:"))
y2 = float(input("Enter y2:"))

squared_difference_x = math.pow(x2 - x1, 2) 
squared_difference_y = math.pow(y2 - y1, 2)
distance = math.sqrt(squared_difference_x + squared_difference_y)
print("Distance between the two points is: {:.2f}".format(distance))
