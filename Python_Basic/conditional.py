
# python calculator
operator = input("Enter a operator(+ - * /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
    print(f"Answer is :{round(result, 3)}")
elif operator == "-":
    result = num1 - num2
    print(f"Answer is :{round(result, 3)}")
elif operator == "*":
    result = num1 * num2
    print(f"Answer is :{round(result, 3)}")
elif operator == "/":
    result = num1 / num2
    print(f"Answer is :{round(result, 3)}")
else:
    print(f"{operator}is an invalid operator!")


# weight converter
unit = input("Choose your weight between kg or lb: ").strip().upper()
weight = float(input("Enter your weight: "))

if unit == "KG":
    weight = weight * 2.20
    unit = "lb"
    print(f"Your Weight is: {round(weight,1)} {unit}")
elif unit == "LB":
    weight = weight / 2.20
    unit = "kg"
    print(f"Your Weight is: {round(weight,1)} {unit}")
else:
    print(f"{unit} is not valid unit!")


# Temperature meter
temp = float(input("Enter your temperature: "))
unit = input("Enter your temperature in Celsius or Fahrenheit (C/F): ")

if unit == "C":
    temp = (temp * 9/5) + 32
    unit = "°F"
    print(f"Temperature is {round(temp,2)}{unit}")
elif unit == "F":
    temp = (temp - 32) * 5/9
    unit = "°C"
    print(f"Temperature is {round(temp,2)}{unit}")
else:
    print("Invalid unit! Please enter C or F.")



# entertainment days
days = input("Enter the name of the day: ").strip().capitalize()

if days == "Saturday":
    print("You can play PUBG.")
elif days == "Sunday":
    print("You can drive bike.")
elif days == "Monday":
    print("You can play guiter.")
elif days == "Tuesday":
    print("You can play sports.")
elif days == "Wednesday":
    print("You can read books.")
elif days == "Thursday":
    print("You can watch movies.")
elif days == "Friday":
    print("You can read holy Quran.")
else:
    print(f"Invalid days name!")


# Voting machine:
age = int(input("Enter your age: "))

if age >= 18:
    print("You are available for cast your vote.")
elif age < 0:
    print("Invalid age!")
else:
    print("You are not a voter!")
    



    
