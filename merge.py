#we have to merge both the list in one dict(one list as key and the another as values)
list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,] 
dic=dict(zip(list1,list2))
print(dic)