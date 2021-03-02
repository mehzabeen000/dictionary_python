#we have to see whether our input exists in the dictionary as key or not
dict={"name":"Raju", "marks":56}
name=input("Enter the key")
for key in dict:
    if name in dict:
        print("Exists")
        break
    else:
        print("Doesn't Exist")
        break