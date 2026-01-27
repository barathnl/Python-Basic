def merge_sort(nums:list[int]):
    # A list with one or zero element is, by definition, sorted!
    if len(nums)<=1:
        return nums

    # 1. Divide: Find the midpoint and split the list
    mid = len(nums) // 2
    left_nums = nums[:mid]
    right_nums = nums[mid:]

    # 2. Conquer: Merge the sorted halves back together
    return sort(merge_sort(left_nums),merge_sort(right_nums))

def sort(left_nums:list[int], right_nums:list[int]) -> list[int]:
    i = j = 0
    sorted_nums =[]

    # Compare elements from both lists and pick the smaller one
    while i<len(left_nums) and j<len(right_nums):
        if left_nums[i]<right_nums[j]:
            sorted_nums.append(left_nums[i])
            i +=1
        else:
            sorted_nums.append(right_nums[j])
            j +=1

    # If there are remaining elements in left or right, add them
    sorted_nums.extend(left_nums[i:])
    sorted_nums.extend(right_nums[j:])

    return sorted_nums

nums = [2,6,2,5,1]
sorted_nums = merge_sort(nums)
print(f"Final sorted number {sorted_nums}")
