nums = list(map(int, input().split()))
k = int(input())
def reverseArray(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums
def reversePartOfTheArray(k, nums):
    reverseArray(nums, 0, len(nums)-1)
    reverseArray(nums, 0, k % len(nums) -1)
    reverseArray(nums, k % len(nums), len(nums)-1)
    return nums
print(reversePartOfTheArray(k, nums))