def insertionSort(nums:list[int]) -> list[int]:
    n = len(nums)
    for i in range(1,n):
        key = nums[i]
        j = i - 1
        print(f"Checking element {key} in {nums}")
        while j>=0 and key<nums[j]:
            nums[j+1] = nums[j]
            print(f"  Shifting {nums[j]} to the right: {nums}")
            j -=1
        nums[j+1] = key
        print(f"  Inserting {key}: {nums}\n")
    return nums

nums = [2,6,2,5,1]
sorted_nums = insertionSort(nums)
print(f"Final sorted number {sorted_nums}")
