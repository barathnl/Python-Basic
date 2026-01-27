def quickSort(nums:list[int]) -> list[int]:
    # A list with one or zero element is, by definition, sorted!
    if len(nums)<=1:
        return nums

    # Picking the pivot (we'll use the last element)
    pivot = nums[-1]
    print(f"Current list: {nums} | Pivot chosen: {pivot}")

    # Partitioning
    left_nums = [x for x in nums[:-1] if x <= pivot]
    right_nums = [x for x in nums[:-1] if x > pivot]

    print(f" Left (<= {pivot}): {left_nums}")
    print(f" Right (> {pivot}): {right_nums}")

    # Recursively sort and combine
    result = quickSort(left_nums) + [pivot] + quickSort(right_nums)
    print(f"Merged result: {result}")
    return result

nums = [2,6,2,5,1]
sorted_nums = quickSort(nums)
print(f"Final sorted number {sorted_nums}")