def bubbleSort(nums:list[int]) -> list[int]:
    n = len(nums)
    for i in range(n):
        for j in range (0,n-i-1,1):
            if nums[j] > nums[j+1]:
                nums[j] , nums [j+1] = nums[j+1], nums[j]
    return nums

nums = [2,6,2,5,1]
sortedNums = bubbleSort(nums)
print(sortedNums)
