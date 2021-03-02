# Python program to combine two dictionary adding values for common keys.
from collections import Counter
dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
dict_new=Counter(dic1)+Counter(dic2)+Counter(dic3)
print(dict_new)

