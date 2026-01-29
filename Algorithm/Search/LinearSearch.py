# Time Complexity: O(n) - In the worst case, you check every single element.
# Memory Complexity: O(1) - No extra memory needed regardless of list size.

def linearSearch(nums: list[int], target: int) -> int:
    """
    Iterates through the list and returns the index of the target.
    Returns -1 if the target is not found.
    """
    # Loop through every index from 0 to n-1
    for i in range(len(nums)):

        # Check if the current element matches our target
        if nums[i] == target:
            # Found it! Return the index immediately and exit the function.
            return i

    # If the loop finishes without returning, the target isn't in the list.
    return -1


# Note: Linear Search does NOT require the list to be sorted.
nums = [3, 1, 10, 7, 9, 11]
target_val = 15

index = linearSearch(nums, target_val)

if index != -1:
    print(f"Target found at index: {index}")
else:
    print(f"Target {target_val} not found in the list.")