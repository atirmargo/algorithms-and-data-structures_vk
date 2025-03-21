list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
def mergeSortedArrays(arr1, arr2):
    mergedList = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if list1[i] < list2[j]:
            mergedList.append(list1[i])
            i += 1
        else:
            mergedList.append(list2[j]) 
            j += 1
    for a in list1[i:]:
        mergedList.append(a)
    for b in list2[j:]:
        mergedList.append(b)
    return mergedList
print(mergeSortedArrays(list1, list2))

        