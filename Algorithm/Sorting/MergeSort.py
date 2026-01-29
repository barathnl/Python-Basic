# Time Complexity: O(n log n) - Very efficient for large datasets
# Memory Complexity: O(n) - Requires extra space to store the divided lists

def merge_sort(nums: list[int]):
    # Base Case: A list with 0 or 1 element is already sorted.
    # This is the "stop" signal for the recursion.
    if len(nums) <= 1:
        return nums

    # 1. DIVIDE: Find the midpoint and split the list into two halves.
    mid = len(nums) // 2
    left_nums = nums[:mid]
    right_nums = nums[mid:]

    # 2. CONQUER: Recursively split and then merge the results.
    # merge_sort() keeps calling itself until it hits the base case.
    return sort(merge_sort(left_nums), merge_sort(right_nums))

def sort(left_nums: list[int], right_nums: list[int]) -> list[int]:
    """
    The 'Merge' helper function. It takes two sorted lists and
    combines them into one single sorted list.
    """
    i = j = 0
    sorted_nums = []

    # Use two pointers (i and j) to walk through both lists.
    # Compare elements and append the smaller one to our result.
    while i < len(left_nums) and j < len(right_nums):
        if left_nums[i] < right_nums[j]:
            sorted_nums.append(left_nums[i])
            i += 1
        else:
            sorted_nums.append(right_nums[j])
            j += 1

    # If one list finishes first, append whatever is left of the other list.
    # Since the input lists were already sorted, these remainders are safe to add.
    sorted_nums.extend(left_nums[i:])
    sorted_nums.extend(right_nums[j:])

    return sorted_nums

# Test Execution
nums = [2, 6, 2, 5, 1]
sorted_nums = merge_sort(nums)
print(f"Final sorted number: {sorted_nums}")