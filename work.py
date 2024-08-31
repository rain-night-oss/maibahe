# a[0..n-i]中查找值最大的元素maxe和元素最小的元素mine。
def find_max_and_min(a):
    if len(a) % 2 == 1:
        maxe = mine = a[0]
        i = 1
    else:
        maxe = mine = a[0]
        i = 2

    while i < len(a) - 1:
        if a[i] > a[i + 1]:
            if a[i] > maxe:
                maxe = a[i]
            if a[i + 1] < mine:
                mine = a[i + 1]
        else:
            if a[i + 1] > maxe:
                maxe = a[i + 1]
            if a[i] < mine:
                mine = a[i]
        i += 2

    if len(a) % 2 == 1:
        if a[-1] > maxe:
            maxe = a[-1]
        elif a[-1] < mine:
            mine = a[-1]

    return maxe, mine


array = list(input("请输入数组:").split())
maxe, mine = find_max_and_min(array)
print("最大元素：" + maxe)
print("最小的元素:" + mine)

# 最好情况：数组已经排序好，但是还是要遍历一遍，时间复杂度为O(n)
# 最坏情况：数组完全逆序，同样遍历所有元素，时间复杂度为O(n)
# 平均情况：无论如何分布，都需要全部遍历一遍，时间复杂度为O(n)