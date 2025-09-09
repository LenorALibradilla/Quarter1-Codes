num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
sum = num1 + num2 + num3
rounded_sum = round(sum, 2)
formatted_sum = "{:.2f}".format(rounded_sum)
print("The total of the three numbers is:", formatted_sum)