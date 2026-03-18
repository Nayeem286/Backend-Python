name = ["nayeem", "akash", "Ridoy", "Anik"]
if "nayeem" in name:
    print("Yes, available in the list")


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:4] = ["blackcurrant", "Lichi", "Berry"]
print(thislist)

list = ["germany", "finland", "norway", "hungary"]
list.insert(1,"poland")
print(list)

list.append("Iceland")
print(list)

list.extend(thislist)
print(list)



## Remove() list
sportsList = ["Football","soccer","cricket","Football","tennis","rugby","golf"]
sportsList.remove("soccer")
print(sportsList)

sportsList.remove("Football")
print(sportsList)

## Pop() list
SportsList = ["Football","soccer","cricket","Football","tennis","rugby","golf"]

SportsList.pop(5)
print(SportsList)

SportsList.pop()
print(SportsList)

# clear() list
SportsList.clear()
print(SportsList)

# delete[] list
Sports_List = ["Football","soccer","cricket","Football","tennis","rugby","golf"]
del Sports_List[0]
print(Sports_List)

del Sports_List
print(Sports_List)