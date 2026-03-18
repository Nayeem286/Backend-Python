name = "Nayeem"
age = 25
print(f"my name is {name} and I'm {age} years old")


#string methods
name = "  hELLO mY naMe Is naYeEm  "
print(name.upper())
print(name.lower())
print(name.strip())

#replace()
name2 = "A bat. A ball. A apple. A football. A cow. A tiger. This is A boy"
print(name2.replace("A", "The")) # "The" will take place instead of "A"
print(name2.replace("A","The",3)) # "The" will take place instead of only 3 "A" 


#Split()
split = "Hello, my name is Nayeem. I live in germany"
print(split.split())

split1 = "Hello, my name is Nayeem. I live in germany"
print(split1.split("."))

split2 = "HelloXmy name is NayeemXI live in Japan"
print(split2.split("X"))

split3 = "Hello*my name is Nayeem*I live in Japan*Its very beautiful country"
print(split3.split("*",1))
print(split3.split("*",2))


#join()
user_words = ["Hello", "how", "are", "you"]
message = " ".join(user_words)
print(message)

user = ["nayeem", "25", "admin"]
separator = "|".join(user)
print(separator)

#find()
text = "Hello, my name is Nayeem. I live in germany"
print(text.find("e",10,24)) #output is 13.Bcz from 10-24 index the 1st "e" in 13th index.
print(text.find("X")) #not available. so -1.


#real-life examples:
email = "nayeem@gmail.com"
if email.find("@") != -1:
    print("Valid email format")


#count()
text1 = "I love apples, apple are my favorite fruit"
print(text1.count("apples")) #find how many apples in the sentence. Only 1
print(text1.count("apples",6,20)) #found only 1 apples within this index.

#real-life examples:
password = "123@nayeem@"
if password.count("@") > 1:
  print("Strong password")
else:
    print("Weak password")


comment = "buy buy buy buy buy buy"
if comment.count("buy",0,7) >= 3:
    print("Spam comment")
else:
    print("Valid comment")
    
    
#startwith()

text2 = "Hi, my name is nayeem"
print(text2.startswith("bye"))
print(text2.startswith("Hi"))
print(text2.startswith("my",4,7))

#endwith()
