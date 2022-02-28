numbers = range(8)

# Expression followed by a for loop followed by a conditional clause.
new_list = [n**2 for n in numbers if n%2 == 0] 

print(new_list)