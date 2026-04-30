"""
PYTHON LIST INTERVIEW CHEAT SHEET
-----------------------------------------------------------------------
Property: Ordered, Mutable, Allows Duplicates, Heterogeneous.

OPERATION      | METHOD           | BIG O    | NOTES
-----------------------------------------------------------------------
Access         | list[i]          | O(1)     | Direct index access.
Append         | .append(x)       | O(1)     | Add to end.
Insert/Delete  | .insert/.pop(i)  | O(n)     | Shifts all later elements.
Search/Remove  | in / .remove(x)  | O(n)     | Linear scan through items.
Sort           | .sort()          | O(n log n)| Timsort (Stable & In-place).
-----------------------------------------------------------------------
"""


def list_revision():
    # 1. Initialization
    # Lists are ordered, changeable, and allow different data types
    numbers = [1, 2, 3, 5, 8, 6, 7, 4]
    mixed_data = [1, 2, 3, 'a', True, "a"]

    print(f"Original List: {numbers}")
    print(f"Mixed Types: {mixed_data}")

    # 2. Deletion Methods
    # .pop() without arguments removes the last item
    numbers.pop()  # O(1)
    print(f"After popping last: {numbers}")

    # .pop(index) removes and returns item at index
    numbers.pop(0)  # O(n) - requires shifting all other elements
    print(f"After popping index 0: {numbers}")

    # .remove(value) removes the first occurrence of that value
    numbers.remove(8)  # O(n) - must search the list first
    print(f"After removing value 8: {numbers}")

    # 3. Addition & Organization
    numbers.append(1)  # O(1)
    print(f"After appending 1: {numbers}")

    numbers.sort()  # O(n log n) - modifies the list in-place
    print(f"Sorted: {numbers}")

    numbers.reverse()  # O(n) - flips the list in-place
    print(f"Reversed: {numbers}")

    # 4. Math & Analysis
    # sum(iterable, start)
    total_sum = sum(numbers)
    print(f"Sum: {total_sum}")

    total_with_offset = sum(numbers, 10)
    print(f"Sum with start value 10: {total_with_offset}")

    # .count(value) returns the frequency of the value
    occurrence_count = numbers.count(5)
    print(f"Frequency of 5: {occurrence_count}")


if __name__ == "__main__":
    list_revision()