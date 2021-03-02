#From the given list we have to take the values in different list and sort the unique values.

list1=[{"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, {"six":"9"},{"seven":"7"}]
list_values=[]
for keys in list1:
    for key,values in keys.items():
        list_values.append(values)
end_list=[]
for element in list_values:
    if element not in end_list:
        end_list.append(element)
print(end_list,"is the sorted unique list")


