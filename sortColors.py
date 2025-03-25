class Solution:
    def sortColors(self, arr):
        low = 0
        middle = 0
        hight = len(arr) - 1
        while middle <= hight:
            if arr[middle] == 0:
                arr[middle], arr[low] = arr[low], arr[middle]
                low += 1
                middle += 1
            elif arr[middle] == 2:
                arr[middle], arr[hight] = arr[hight], arr[middle]
                hight -= 1
            else:
                middle += 1
        return arr
arr = list(map(int, input().split()))
solution = Solution()
print(solution.sortColors(arr))