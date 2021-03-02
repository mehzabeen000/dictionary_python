dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 
          'David': ['subj1', 'subj2']}
count=0
for values in dict.values():
    for i in values:
        count+=1
print(count,"is the count of values in list")

    

