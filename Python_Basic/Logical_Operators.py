
is_admin = True
is_banned = False

if is_admin and not is_banned:
    print("Access to admin panel granted")
else:
    print("Access denied")


#Food panda app
is_premium_user = True
discount = int(input("Enter order amount: "))

if discount >= 1500 or is_premium_user:
    print(f'You get 20% discount')
else:
    print(f'To get 20% discount.Order more then 1500')


# OR operator   
age = int(input("Enter your age: "))
citizenship = input("Enter your citizenship: ").strip().upper()
gender = input("Enter your gender(Male or Female): ").strip().capitalize()

if age > 18 or citizenship == "USA" or gender == "Male":
    print(f"You will go to night club")
else:
    print(f"You are not allowed")
    

#login system
password = "1234"
email = "nnayeem205@gmail.com"
role = "admin"
login = input("Enter your password or email or role: ")

if login == password or login == email or login == role:
    print("You can logged in.")
else:
    print("Invalid login.")
 
    
Password = int(input("Enter your password: "))
Email = input("Enter your email: ").strip().lower()
Role = input("Enter your role: ").strip().lower()

if Password == "12345" or Email == "nn205@gmail.com" or Role == "admin":
    print("You can login.")
else:
    print("You cannot login.")



password = "123"
email = "n205@gmail.com"

user_pass = input("Enter your password: ")
user_email = input("Enter your email: ")

if user_pass == password and user_email == email:
    print("Login successfully")
else:
    print("Invalid Password or Email")



password = "123"
email = "n205@gmail.com"

user_email = input("Enter your email: ")
user_pass = input("Enter your password: ")

if user_email != email:
    print("Invalid email")
elif user_pass != password:
    print("Invalid Password")
else:
    print("Login successfully")


soap = 60
pizza = 500
shampoo = 750
milk = 110
soft_drinks = 25

soap = float(input("Enter soap quantity: "))
pizza = float(input("Enter pizza quantity: "))
shampoo = float(input("Enter shampoo quantity: "))
milk = float(input("Enter milk quantity: "))
soft_drinks = float(input("Enter soft-drinks quantity: "))

soap_prize = 60 * soap
pizza_prize = 500 * pizza
shampoo_prize= 750 * shampoo
milk_prize = 110 * milk
softDrinks_prize = 25 * soft_drinks

total_cost = soap_prize + pizza_prize + shampoo_prize + milk_prize + softDrinks_prize
print(f'Total bill: {total_cost} taka')

if total_cost >= 3000:
    discount = total_cost * 0.20
    print(f'You get 20% discount')
elif total_cost >= 1500:
    discount = total_cost * 0.10
    print(f'You get 10% discount')
else:
    discount = 0
    print(f'No discount')
    
final_price = total_cost - discount
print(f'Your bill after discount:{final_price} taka')
