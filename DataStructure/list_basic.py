# Python list - List is ordered, changeable, allow duplicate, allow different dataType
class MyList:

    def __init__(self):
        self.list_var = [1, 2, 3]  # Square bracket [] is used to define list

    def __str__(self):
        return f"MyList Object: {self.list_var}"

    def access_list(self, index):
        if 0 <= index < len(self.list_var):
            return self.list_var[index]  # List is access by index , starting from 0 to n-1 when n is length of list
        else:
            return "Index out of bounds"

    def update_list(self, index, replaceValue):
        if 0 <= index < len(self.list_var):
            self.list_var[index] = replaceValue  # Update an element at a specific index
            print(f"List updated: {self.list_var}")
        else:
            print("Cannot update: Index out of bounds")

    def sort_list(self):
        # The sort() method sorts the list in-place and returns None.
        # It works for lists with elements of the same comparable type (e.g., all numbers or all strings).
        print("Before sorting:", self.list_var)
        self.list_var.sort()
        print("After sorting:", self.list_var)

    def remove_elements(self, value_to_remove=None, index_to_pop=None, remove_all=False):
        """
        Optimized removal:
        - index_to_pop: O(1) if at the end, O(n) if at the start.
        - value_to_remove: O(n) because it must search.
        - remove_all: A 'Pythonic' way to clear all instances of a value.
        """
        # 1. Handle Index-based removal (Faster if you know the position)
        if index_to_pop is not None:
            try:
                removed_item = self.list_var.pop(index_to_pop)
                print(f"Popped index {index_to_pop}: {removed_item}")
            except IndexError:
                print(f"Error: Index {index_to_pop} is out of range.")

        # 2. Handle Value-based removal
        if value_to_remove is not None:
            if remove_all:
                # List comprehension is the fastest way to "remove all"
                # Time Complexity: O(n)
                self.list_var = [item for item in self.list_var if item != value_to_remove]
                print(f"Removed all instances of {value_to_remove}.")
            else:
                # Standard remove (only first occurrence)
                # Time Complexity: O(n)
                if value_to_remove in self.list_var:
                    self.list_var.remove(value_to_remove)
                    print(f"Removed first occurrence of {value_to_remove}.")
                else:
                    print(f"Value {value_to_remove} not found.")

    def append_element(self, element_to_add):
        """Appends an element to the end of the list."""
        self.list_var.append(element_to_add)
        print(f"Appended '{element_to_add}'. List: {self.list_var}")

    def loop_list(self):
        """Iterates through the list and prints each element."""
        print("\nLooping through the list:")
        for item in self.list_var:
            print(item)

        for index , value in enumerate(self.list_var):
            print(f"Value at index {index} is {value}")

        print("\nReverse Looping through the list:")
        for item in reversed(self.list_var):
            print(item)


# Instance (a.k.a object) creation
list_instance = MyList()

print(list_instance)

print("\n--- access_list ---")
index = 0
element = list_instance.access_list(index)
print(f"Element at index {index} is {element}")

print("\n--- update_list ---")
list_instance.update_list(1, 99)
print(list_instance)
list_instance.update_list(10, 500)  # Test out of bounds update

print("\n--- sort_list ---")
# To demonstrate sort, let's reset or add elements that can be sorted
list_instance = MyList()  # Re-initialize for a clean sort demo
list_instance.list_var = [3, 1, 4, 1, 5, 9, 2]  # Example list
list_instance.sort_list()
print(list_instance)

print("\n--- remove_elements ---")
list_instance = MyList()  # Re-initialize for a clean remove demo
list_instance.list_var = [1, 99, 2, 3, 99, 4,2]  # Example list for removal
print(list_instance)
list_instance.remove_elements(value_to_remove=99)  # Remove first occurrence of 99
print(list_instance)
list_instance.remove_elements(index_to_pop=0)  # Pop element at index 0
print(list_instance)
list_instance.remove_elements(value_to_remove=100)  # Value not found
print(list_instance)
list_instance.remove_elements(index_to_pop=10)  # Index out of bounds
print(list_instance)
list_instance.remove_elements(value_to_remove=2,remove_all=True)
print(list_instance)

print("\n--- append_element ---")
list_instance = MyList()  # Re-initialize for a clean append demo
list_instance.append_element(4)
list_instance.append_element("hello")
print(list_instance)

print("\n--- loop_list ---")
list_instance = MyList()  # Re-initialize
list_instance.list_var = [1, 2, 5, 3, 99, 2]
list_instance.loop_list()