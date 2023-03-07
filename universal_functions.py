import numpy as np

###################### 1. 最大值 #################################
def maximum(list):
    max = np.max(list)
    return max


###################### 2. 最小值 #################################
def minimum(list):
    min = np.min(list)
    return min

###################### 3. 快速排序 #################################
def quickSort(lists,i,j):
    if i >= j:
        return list
    pivot = lists[i]
    low = i
    high = j
    while i < j:
        while i < j and lists[j] >= pivot:
            j -= 1
        lists[i]=lists[j]
        while i < j and lists[i] <=pivot:
            i += 1
        lists[j]=lists[i]
    lists[j] = pivot
    quickSort(lists,low,i-1)
    quickSort(lists,i+1,high)
    return lists

###################### 4.冒泡排序 #################################
def bubbleSort(lists):
    n = len(lists)
 
    for i in range(n):
        for j in range(0, n-i-1):
            if lists[j] > lists[j+1] :
                lists[j], lists[j+1] = lists[j+1], lists[j]
    
    return lists

###################### 5.求和 #################################
def sum(list):
    sum = np.sum(list)
    return sum

###################### 6.平均 #################################
def avg(list):
    avg = np.average(list)
    return avg

###################### 7.查找第k大/小 #################################
import heapq

def findKthLargest(lists, k):
    stack = []
    for num in lists:
        heapq.heappush(stack, lists)
        if len(stack) > k:
            stack.pop()
    return stack[-1]

def findKthSmallest(lists, k):
    for i in range(k):
        for j in range(i + 1, len(lists)):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists[k-1]

###################### 8.中位数 #################################
def median(list):
    list.sort()
    half = len(list) // 2
    return (list[half] + list[~half]) / 2

###################### 9.众数 #################################
import statistics

def mode(list):
    return statistics.mode(list)

###################### 10.方差 #################################
def variance(list):
    return np.var(list)

###################### 11.标准差 #################################
def standard(list):
    return np.std(list, ddof=1)

###################### 12.交换 #################################
def exchange(list, i, j):
    list[i],list[j] = list[j],list[i]
    return list
