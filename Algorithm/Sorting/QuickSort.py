# Time Complexity: O(n log n) - Average/Best case
# Time Complexity: O(n^2) - Worst case (if pivot is always the min/max)
# Memory Complexity: O(n) - In this specific Pythonic implementation (due to list comprehensions)

def quickSort(nums: list[int]) -> list[int]:
    # BASE CASE: If the list is empty or has one item, it's already sorted.
    # This prevents infinite recursion.
    if len(nums) <= 1:
        return nums

    # 1. PICK A PIVOT: We are using the last element as the "benchmark."
    pivot = nums[-1]
    print(f"Current list: {nums} | Pivot chosen: {pivot}")

    # 2. PARTITIONING:
    # Create two sub-lists:
    # - left_nums: Everyone smaller than or equal to the pivot.
    # - right_nums: Everyone larger than the pivot.
    # We slice [:-1] to exclude the pivot itself from these lists.
    left_nums = [x for x in nums[:-1] if x <= pivot]
    right_nums = [x for x in nums[:-1] if x > pivot]

    print(f"  Left (<= {pivot}): {left_nums}")
    print(f"  Right (> {pivot}): {right_nums}")

    # 3. RECURSE & COMBINE:
    # Sort the left, put the pivot in the middle, and sort the right.
    # The pivot is now in its "final" sorted position.
    result = quickSort(left_nums) + [pivot] + quickSort(right_nums)

    print(f"Merged result: {result}")
    return result


# Test Execution
nums = [2, 6, 2, 5, 1]
sorted_nums = quickSort(nums)
print(f"\nFinal sorted number: {sorted_nums}")