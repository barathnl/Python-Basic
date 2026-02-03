#Python set - Set is unordered, unindexed , does not allow duplicate, contain different data types: string, integer and boolean
color_set = {'red' , 'blue' , 'green' , 'red'}
complex_color = {'crimson red'}
number_list = [999]
boolean_set= {1, True , 0 , False}

#Ways to add value
color_set.add('yellow')
color_set.update(complex_color)
color_set.update(number_list)

#Ways to remove value
color_set.remove(999) # item to remove does not exist, remove() will raise an error.
color_set.discard(999) # item to remove does not exist, remove() will NOT raise an error.

print(color_set)
print(boolean_set)
print(type(color_set))
print(len(color_set))
print('red' in color_set)


#Joining set
set1 = {"a", "b", "c"}
set2 = {1, 2, 3, "a"}
print(f'Set 1 : {set1}')
print(f'Set 2 : {set2}')

print('#Union ( set 1 | set 2 ) - will return a new set with all items from both sets.')
set3_m= set1.union(set2)
set3_op= set1 | set2
print(set3_op)
print(set3_m)

print('#Intersection ( set 1 & set 2 ) - will return a new set, that only contains the items that are present in both sets')
set4_m= set1.intersection(set2)
set4_op= set1 & set2
print(set4_m)
print(set4_op)

print('#Difference ( set 1 ^ set 2 ) - return a new set that will contain only the items from the first set that are not present in the other set')
set5_m= set1.difference(set2)
set5_op= set1 - set2
print(set5_m)
print(set5_op)

print('#Symmetric Differences ( set 1 ^ set 2 ) - will keep only the elements that are NOT present in both sets.')
set6_m= set1.symmetric_difference(set2)
set6_op= set1 ^ set2
print(set6_m)
print(set6_op)
