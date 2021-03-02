#Python program to print all unique values in a dictionary. Go to the editor
dic=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
u_value = set( val for L in dic for val in L.values())
print("Unique Values: ",u_value)