nums = list(map(int, input().split()))
class Solution:
    def reverseArray(self, nums):
        left = 0
        right = len(nums)-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums
solution = Solution()
print(solution.reverseArray(nums))