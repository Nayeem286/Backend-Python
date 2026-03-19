"""
# OR operator   
age = int(input("Enter your age: "))
citizenship = input("Enter your citizenship: ").strip().upper()
gender = input("Enter your gender: ").strip().capitalize()

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
""" 
