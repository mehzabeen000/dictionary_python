# Python script to sort (ascending and descending) a dictionary by value.
dict_names={'bijender':45,'deepak':60,'param':20,'anjali':30,'roshini':50}
dict1 = sorted(dict_names.items(), key=lambda x: x[1])    
print(dict1)    



dict_names={'bijender':45,'deepak':60,'param':20,'anjali':30,'roshini':50}
dict1 = sorted(dict_names.items(), key=lambda x: x[1],reverse=True)
print(dict1)    
    