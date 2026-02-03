#Python tuple - Tuple is ordered, allow duplicates, unchangeable and accessed by index, contain different data types: string, integer and boolean
fruit_tuple = ('apple', 'banana', 'apple', 'orange', 99, True)

print(fruit_tuple)
print(len(fruit_tuple))
print(fruit_tuple[0])
print(fruit_tuple[-1])

# Tuple unpacking
fruit1, fruit2, fruit3, fruit4, amt, isSold = fruit_tuple
print(fruit2)
print(amt)
print(isSold)