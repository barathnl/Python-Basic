"""
PYTHON TUPLE INTERVIEW CHEAT SHEET
-----------------------------------------------------------------------
Property: Ordered, Unchangeable (Immutable), Allows Duplicates.

OPERATION      | METHOD / SYNTAX  | BIG O    | NOTES
-----------------------------------------------------------------------
Access         | tuple[i]         | O(1)     | Fast index-based access.
Unpacking      | a, b = tuple     | O(n)     | Maps elements to variables.
Search         | x in tuple       | O(n)     | Linear scan.
Count/Index    | .count(), .index()| O(n)    | Search operations.
-----------------------------------------------------------------------
Note: Tuples use less memory than lists and are "Hashable" (can be
      used as dictionary keys) if they contain only immutable items.
"""


def tuple_revision():
    # 1. Initialization
    # Tuples are ordered, allow duplicates, and are unchangeable (immutable)
    # They can contain different data types: string, integer, boolean, etc.
    fruit_items = ('apple', 'banana', 'apple', 'orange', 99, True)

    print(f"Original Tuple: {fruit_items}")
    print(f"Length of Tuple: {len(fruit_items)}")

    # 2. Accessing Data (O(1))
    # Accessed by index just like lists
    first_item = fruit_items[0]
    last_item = fruit_items[-1]

    print(f"First Item: {first_item}")
    print(f"Last Item: {last_item}")

    # 3. Tuple Unpacking (O(n))
    # This is a very common Pythonic way to assign multiple variables at once.
    # Note: The number of variables must match the number of items in the tuple.
    item1, item2, item3, item4, amount, is_sold = fruit_items

    print("\n--- Unpacking Results ---")
    print(f"Fruit 2: {item2}")
    print(f"Amount: {amount}")
    print(f"Is Sold: {is_sold}")

    # 4. Useful Tuple Methods
    # Since tuples are immutable, they only have two methods: .count() and .index()
    apple_count = fruit_items.count('apple')
    banana_index = fruit_items.index('banana')

    print(f"\nApples found: {apple_count}")
    print(f"Index of 'banana': {banana_index}")


if __name__ == "__main__":
    tuple_revision()