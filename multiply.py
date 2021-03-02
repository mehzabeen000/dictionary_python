#Python program to multiply all the items in a dictionary.
dict1={'apple':40,"banana":60,"orange":80}
multiply=1
for values in dict1.values():
    multiply=multiply*values
print(multiply)