#we have to print the count occurence of element present in the given string.
str="MISSISSIPPI"
newstr=[]
for element in str:
    if element not in newstr:
        newstr.append(element)
i = 0 
dict={}
while(i < len(newstr)):
    j = 0
    count =0
    while j < len(str):
        if newstr[i] in str[j]:
            count +=1
        j = j + 1
    dict[newstr[i]]=count
    i = i + 1
print(dict)
