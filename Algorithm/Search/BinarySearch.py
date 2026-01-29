# Time Complexity: O(log n) - Extremely fast; cuts the search area in half every step.
# Memory Complexity: O(log n) - Due to the recursion stack (O(1) if done with a loop).

def binarySearch(nums: list[int], target: int, left: int, right: int):
    # BASE CASE: The search window has closed (left and right crossed).
    # If we haven't found the target by now, it's not in the list.
    if left > right:
        return -1

    # 1. FIND THE MIDPOINT: Integer division (//) gives us a whole number index.
    middle = (left + right) // 2

    # 2. MATCH FOUND: Return the index immediately.
    if nums[middle] == target:
        return middle

    # 3. SEARCH LEFT: If the midpoint value is too big, the target must be on the left.
    if nums[middle] > target:
        # We search from the current 'left' to 'middle - 1'
        return binarySearch(nums, target, left, middle - 1)

    # 4. SEARCH RIGHT: If the midpoint value is too small, the target must be on the right.
    if nums[middle] < target:
        # We search from 'middle + 1' to the current 'right'
        return binarySearch(nums, target, middle + 1, right)

# NOTE: Binary Search ONLY works on lists that are already SORTED.
nums = [1, 3, 5, 7, 9, 11]
n = len(nums)
index = binarySearch(nums, 3, 0, n - 1)
print(f"Target found (or insertion point) at index: {index}")