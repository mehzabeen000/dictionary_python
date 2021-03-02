#we have to compare the values,sort them and print the 3 highest value from them.
my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
list1=[]
for values in my_dict.values():
    list1.append(values)
i=0
while i<len(list1):
    j=0
    while j<(len(list1)-1):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
        j+=1
    i+=1
print(list1[-3:])