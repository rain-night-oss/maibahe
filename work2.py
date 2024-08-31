#a[0..n-i]中查找值最大的前k个元素maxe_k和元素最小的后k个元素mine_k。
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

array=list(input("请输入一个数组:").split())
array=bubble_sort(array)
k=int(input("请输入一个整数："))
maxe_k=array[-k:]
mine_k=array[:k]
print("前k个最大的元素组成的数组：" ,maxe_k)
print("后k个最小的元素组成的数组：",mine_k)
#最好情况：已经排序好，只需要遍历一遍，时间复杂度为O(n)
#最坏情况：逆序，需要进行n-1次遍历，每次遍历需要比较n-1次，时间复杂度为O(n^2)
#平均情况：时间复杂度O(n^2)