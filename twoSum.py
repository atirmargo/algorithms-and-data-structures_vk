nums = []
ls = input().split()
for i in ls:
    nums.append(int(i))
target = int(input())
class Solution:
    def twoSum(self, nums, target):
        left = 0
        right = len(nums)-1
        while left < right:
            a = nums[left]+nums[right]
            if a == target:
                return [left, right]
            elif a > target:
                right -= 1
            elif a < target:
                left += 1
        return[]
solution = Solution()
print(solution.twoSum(nums, target))