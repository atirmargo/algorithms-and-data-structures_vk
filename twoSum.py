num = []
ls = input().split()
for i in ls:
    num.append(int(i))
target = int(input())
def twoSum(num, target):
    left = 0
    right = len(num)-1
    while left < right:
        a = num[left]+num[right]
        if a == target:
            return [left, right]
        elif a > target:
            right -= 1
        elif a < target:
            left += 1
    return[]
print(twoSum(num, target))