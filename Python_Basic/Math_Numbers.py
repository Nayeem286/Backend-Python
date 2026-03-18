# Lesson 2

soup = 10
burger = 8 * 3
ice_cream = 5 
Total = soup + burger + ice_cream
print(f'Total cost is: ${Total}')

pay = Total/3
print(f'Each person pays: ${pay}')

Toaster = 18.50 * 100
T_shirt = 7.50 * 2 * 100
Cost_total = round((Toaster + T_shirt)/100)
print(f'Total cost of toaster and t-shirt: ${Cost_total}')

tax = round(Cost_total * 0.1)
print(f'10% Tax on total cost: ${tax}')

tax = round(Cost_total * 0.2)
print(f'20% Tax on total cost: ${tax}')

toaster = 18.99 * 100
Basketball = 20.95 * 100
t_shirt = 7.99 * 100
bill = (toaster + Basketball + t_shirt)/100
print(f'Total bill: ${bill}')

shipping_bill = bill + 4.99
print(f'Shipping cost: ${shipping_bill}')

Taxx = shipping_bill * 0.1
print(f'10% of tax: ${Taxx}')

Total_Bill = shipping_bill + Taxx
x = round(Total_Bill,2)
print(f'Total bill after 10% of tax: ${x}')

import math
x = math.floor(2.8)
y = math.ceil(2.2)
print(f'Value of x: {x} and y: {y}')

celsius_1 = 25
fahrenheit_1 = (celsius_1 * 9/5) + 32
print(f'Temperature in Fahrenheit: {int(fahrenheit_1)}F')

fahrenheit_2 = 86
celsius_2 = (fahrenheit_2 - 32) * 5/9
print(f'Temperature in Celcius: {int(celsius_2)}C')

celsius_3 = -5
fahrenheit_3 = (celsius_3 * 9/5) + 32
print(f'Temperature in Fahrenheit: {int(fahrenheit_3)}F')
