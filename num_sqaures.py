#we have to take 1 to 15 numbers as key and squares as their values in dictionary
dict={}
square=0
for i in range(1,16):
    square=i**2
    dict[i]=square
print(dict)

