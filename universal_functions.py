import numpy as np

###################### 1. 最大值 #################################
def maximum(list):
    max = list[1]
    for i in range(len(list)):
        if list[i]>max:
            max = list[i]
    return max

###################### 2. 最小值 #################################
def minimum(list):
    min = list[1]
    for i in range(len(list)):
        if list[i]<min:
            min = list[i]
    return min

###################### 3. 快速排序 #################################
def quickSort(lists,i,j,asc):
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
    if asc==1:
        return lists
    if asc==0:
        return list(reversed(lists))

###################### 4.冒泡排序 #################################
def bubbleSort(lists, asc):
    n = len(lists)
 
    for i in range(n):
        for j in range(0, n-i-1):
            if lists[j] > lists[j+1] :
                lists[j], lists[j+1] = lists[j+1], lists[j]
    
    if asc==1:
        return lists
    if asc==0:
        return list(reversed(lists))

###################### 5.求和 #################################
def sum(list, i=None, j=None):
    if i==None and j==None:
        sum = np.sum(list)
    else:
        sum = np.sum(list[i-1:j])
    return sum

###################### 6.平均 #################################
def avg(list, i=None, j=None):
    if i==None and j==None:
        avg = np.average(list)
    else:
        avg = np.average(list[i-1:j])
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

def findKth(lists, k, large):
    if large==1:
        findKthLargest(lists, k)
    if large==0:
        findKthSmallest(lists, k)

###################### 8.中位数 #################################
def median(list):
    list.sort()
    half = len(list) / 2
    if type(half) == int:
        return list[int(half)-1]
    else:
        return list[int(np.ceil(half))-1]

def medianUseAvg(list):
    list.sort()
    half = len(list) // 2
    return (list[half] + list[~half]) / 2

###################### 9.众数 #################################
import statistics

def mode(list):
    return statistics.mode(list)

def modeWithFrequency(list):
    number = statistics.mode(list)
    count = list.count(number)
    return number, count

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
