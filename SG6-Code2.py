radius = float(input("Enter the radius of the circle: "))
area = 3.1416 * radius * radius
rounded_area = round(area, 2)
formatted_area = "{:.2f}".format(rounded_area)
print("The area of the circle is:", formatted_area, "square units")