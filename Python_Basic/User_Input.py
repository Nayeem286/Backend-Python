# Area calculation
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
print(f"Total area is {area} meter")

#shopping 
item = input("Enter your item:")
quantity = int(input("How many you wanna buy?:"))
price = float(input("what's the price of each item?:"))
total = quantity * price
print(f"You have brought {quantity} {item}")
print(f"Total bill is ${total}")

# Average of two number
number1 = int(input("Enter first number:"))
number2 = int(input("Enter second number:"))
sum = (number1 + number2)/2
print(f"Average of two numbers:{sum}")

#circle 
import math
value = float(input("Enter a value of radius: "))
radius = math.pi * (pow(value,2)) 
print(f"The radius of circle is: {round(radius,2)}cm")

#hyperbola 
import math
a = float(input("Enter a value of A:"))
b = float(input("Enter a value of B:"))
hyperbola = math.sqrt(pow(a,2) + pow(b,2))
print(f"The result of hyperbola: {round(hyperbola,2)}")