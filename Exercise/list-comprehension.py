
numbers = range(8)
print(numbers)

# Initialize a new list
nuevaLista = []
# Add values to 'nuevaLista'
for n in numbers:
    if n % 2 == 0: #check if the element is even
        nuevaLista.append(n**2) #raise that element to the power of 2 and append to the list

# Print nuevaLista
print(nuevaLista)


