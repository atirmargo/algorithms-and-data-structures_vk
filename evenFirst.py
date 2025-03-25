class Solution:
    def evenFirst(self, arr):
        even = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 0:
                arr[i], arr[even] = arr[even], arr[i]
                even += 1
        return arr
solution = Solution()
arr = list(map(int, input().split()))
print(solution.evenFirst(arr))