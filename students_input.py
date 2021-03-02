#we have to take 10 user input of student and marks and store them in the dictionary
dic={}
for i in range(0,11):
    name=input("Enter the student name")
    marks=int(input("Enter the marks"))
    dic[name]=marks
print(dic)

