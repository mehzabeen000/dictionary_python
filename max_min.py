dict1={1:20,2:40,7:80,3:45}
a=[]
for values in dict1.values():
    a.append(values) 
print(max(a),"is the maximum value" )
print(min(a),"is the minimum value")
