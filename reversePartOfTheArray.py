nums = list(map(int, input().split()))
k = int(input())
class Solution:
    def reverseArray(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums
    def reversePartOfTheArray(self, k, nums):
        self.reverseArray(nums, 0, len(nums)-1)
        self.reverseArray(nums, 0, k % len(nums) -1)
        self.reverseArray(nums, k % len(nums), len(nums)-1)
        return nums
solution = Solution()
print(solution.reversePartOfTheArray(k, nums))