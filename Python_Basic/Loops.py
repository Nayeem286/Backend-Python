
foods = ["beef","pizza","burger","kacchi","ice-cream","choclate"]
for f in foods:
    if f == "burger":
        print("Order it");
        break;
    print("My ordered foods: ", f)
    
    
    
#while loop
x = 1
while x < 10:
    if x == 3:
        break;
    print(x)
    x += 1
    
    
j = 1
while j < 10:
    if j == 5:
        j += 1
        continue
    print(j)
    j += 1
    
    
i = 0
while i <= 20:
    if i == 16:
        i += 2
        continue
    print(i)
    i += 2
    
x = 1
while x < 10:
    print(x)
    x += 1
else:
    print("Greater than 10")
    
    
    
    
i = 0
while i < 6:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
    


i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  
# form validation projects example of continue
user = ["nayeem", "leo", "", "Rony", "", "suman"]
for name in user:
    if name == "":
        continue
    print("Valid user: ", name)
    






# for loop with break statement
cars = ["bmw","audi","ford","benz","toyota","honda"]

for c in cars:
    print(f'Cars collection {c}')
    if c == "benz":
        print(f'I got my car')
        break
    
    
    
# for loop with continue statement
foods = ["cake","burger","pizza","milk"]  

for f in foods:
    if f == "pizza":
        continue
    print(f'Order: {f}')
    

#while loop with continue statement
i = 1
while i <= 10:
    if i == 6:
        i += 1
        continue
    print(i)
    i += 1
    
    
#while loop with break statement
i = 1;
while i < 10:
    if i == 8:
        break;
    print("value of i is: ", i)
    i += 1
    
#range()
    
for y in range(3,10,2):
    print(y)
    
