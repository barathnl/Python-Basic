# Python Dictionaries - Dictionaries is ordered, changeable, does not allow duplicate, allow different dataType
person_dict = {
    "first name":"abc",
    "age" : 19, # Duplicate key are not allowed
    "age": 20
}

person_dict_const = dict(first_name ="John", age=29)

# Ways to add value
person_dict["zip code"] = "94538" # adding new entry to dict at end
person_dict.update({"zip code":"94540"})

# Ways to change/update value
person_dict["age"] = 21
person_dict.update({"age":22})

print(person_dict)
print(len(person_dict))
print(person_dict.keys()) # Return all keys
print(person_dict.values()) # Return all values
print(person_dict["age"]) # Return value of key 'age'
print(person_dict.get("age")) # Return value of key 'age'
print(person_dict.get("address")) # Return None if not present
print("zip code" in person_dict) # Return True of False

# The setdefault() method returns the value of the item with the specified key. If the key does not exist, insert the key, with the specified value
x = person_dict.setdefault("zip code","11111")
print(x)
x = person_dict.setdefault("country","USA")
print(x)

dict_2 = person_dict.copy() #Copy to new dict

dict_2.pop("age") # Remove specific key
dict_2.popitem() # Remove last key
print(dict_2)

print("\n--- Looping key and value of dict ---")
for key, value in person_dict.items():
    print(key, value)

