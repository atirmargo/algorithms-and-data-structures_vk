class Solution:
    def nullsToEnd(self, arr):
        null = len(arr) - 1
        i = 0
        while i < null:
            while arr[null] == 0:
                null -= 1
            if arr[i] == 0:
                arr[i], arr[null] = arr[null], arr[i]
                null -= 1
            i += 1
        return arr
solution = Solution()
arr = list(map(int, input().split()))
print(solution.nullsToEnd(arr))    