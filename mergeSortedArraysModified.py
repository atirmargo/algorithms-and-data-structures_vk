list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
class Solution:
    def mergeSortedArrays(self, arr1, arr2):
        for i in range(0, len(arr2)):
            arr1.append(0)
        pointer1 = len(arr1)-len(arr2)-1
        pointer2 = len(arr2)-1
        pointer3 = len(arr1)-1
        while pointer2 >= 0:
            if pointer1 >= 0:
                if arr1[pointer1] > arr2[pointer2]:
                    arr1[pointer3] = arr1[pointer1]
                    pointer1 -= 1
                else:
                    arr1[pointer3]=arr2[pointer2]
                    pointer2 -= 1
            pointer3 -= 1
        return arr1
solution = Solution()
print(solution.mergeSortedArrays(list1, list2))
