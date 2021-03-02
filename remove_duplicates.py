# Python program to remove duplicates from Dictionary.
dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
result = {}
for key,value in dic.items():
    if value not in result.values():
        result[key] = value
print(result)
