"""
PYTHON SET INTERVIEW CHEAT SHEET
-----------------------------------------------------------------------
Property: Unordered, Unindexed, No Duplicates, Mutable.

OPERATION      | METHOD            | BIG O    | NOTES
-----------------------------------------------------------------------
Add            | .add(x)           | O(1)     | Instant addition.
Remove/Discard | .remove(x)        | O(1)     | Instant removal.
Membership     | "x" in set        | O(1)     | Fast existence check.
Union          | set1 | set2       | O(n+m)   | All unique elements.
Intersection   | set1 & set2       | O(min(n,m))| Only common elements.
-----------------------------------------------------------------------
Note: Elements must be immutable (hashable).
Note: {1, True} are treated as duplicates because 1 == True in Python.
"""


def set_revision():
    # 1. Initialization
    # Sets are unordered and do not allow duplicates.
    colors = {'red', 'blue', 'green', 'red'}  # Second 'red' is ignored
    complex_colors = {'crimson red'}
    numbers_to_add = [999]

    # TRAP: Python treats 1 and True as the same value, and 0 and False as the same.
    # The first one encountered in the set is the one kept.
    boolean_collision = {1, True, 0, False}

    print(f"Initial Set: {colors}")
    print(f"Boolean Collision Set: {boolean_collision}")

    # 2. Adding Values
    colors.add('yellow')  # Adds a single element
    colors.update(complex_colors)  # Merges another set
    colors.update(numbers_to_add)  # Merges a list into the set
    print(f"After Additions: {colors}")

    # 3. Removing Values
    # .remove() raises KeyError if item is missing.
    # .discard() stays silent if item is missing (safer).
    colors.discard(999)
    if 'red' in colors:
        colors.remove('red')

    # 4. Set Properties
    print(f"Type: {type(colors)} | Length: {len(colors)}")
    print(f"Is 'blue' present? {'blue' in colors}")  # O(1) lookup

    # 5. Joining Sets (Mathematical Operations)
    chars = {"a", "b", "c"}
    mixed = {1, 2, 3, "a"}

    print(f"\nSet A: {chars}")
    print(f"Set B: {mixed}")

    # Union: All items from both (O(len(A) + len(B)))
    union_set = chars.union(mixed)  # or chars | mixed
    print(f"Union (|): {union_set}")

    # Intersection: Only common items (O(min(len(A), len(B))))
    intersection_set = chars.intersection(mixed)  # or chars & mixed
    print(f"Intersection (&): {intersection_set}")

    # Difference: Items in A NOT in B (O(len(A)))
    difference_set = chars.difference(mixed)  # or chars - mixed
    print(f"Difference (-): {difference_set}")

    # Symmetric Difference: Items in EITHER A or B, but NOT both
    sym_diff_set = chars.symmetric_difference(mixed)  # or chars ^ mixed
    print(f"Symmetric Difference (^): {sym_diff_set}")

    # 6. Looping
    print("\n--- Iterating over Set ---")
    for color in colors:
        print(f"Color: {color}")


if __name__ == "__main__":
    set_revision()