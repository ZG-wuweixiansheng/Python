#查找与排序算法
#顺序查找：无序表查找
def sequentialSearch(alist,item):
    pos=0
    found=False
    while pos<len(alist) and not found:
        if alist[pos]==item:
            found=True
        else:
            pos+=1
    return found
result=sequentialSearch([1,3,5,7,9],7)
#print(result)

#顺序查找：有序表查找
def orderedsequentialSearch(alist,item):
    pos=0
    found=False
    stop=False
    while pos <len(alist) and not found and not stop:
        if alist[pos]==item:
            found=True
        else:
            if alist[pos]>item:
                stop=True
            else:
                pos+=1
    return found

#有序表二分法查找
def binarySearch(alist,item):
    first=0
    last=len(alist)-1
    found=False
    while first<=last and not found:
        midpoint=(first+last)//2
        if alist[midpoint]==item:
            found=True
        elif alist[midpoint]<item:
            first=midpoint+1
        else:
            last=midpoint-1
    return found
#print(binarySearch([1,3,5,7,9],1))
#递归算法实现二分查找
def binarySearch1(alist,item):
    if len(alist)==0:
        return False
    else:
        midpoint=len(alist)//2
        if alist[midpoint]==item:
            return True
        else:
            if alist[midpoint]<item:
                return binarySearch1(alist[midpoint+1:],item)
            else:
                return binarySearch1(alist[:midpoint],item)
#冒泡排序
def bubbleSort(alist):
    for passum in range(len(alist)):
        for i in range(len(alist)-passum-1):
            if alist[i]>alist[i+1]:
                temp=alist[i]
                alist[i]=alist[i+1]
                alist[i+1]=temp
    return alist
#print(bubbleSort([23,21,22,16,18]))

#选择排序
def selectionSort(alist):
    for passum in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,1+passum):
            if alist[location]>alist[positionOfMax]:
                positionOfMax=location
        temp=alist[passum]
        alist[passum]=alist[positionOfMax]
        alist[positionOfMax]=temp
    return alist
#print(selectionSort([12,32,11,26,22]))

#插入排序
def insertSort(alist):
    for index in range(1,len(alist)):
        currentvalue=alist[index]
        position=index
        while position>0 and currentvalue<alist[position-1]:
            alist[position]=alist[position-1]
            position-=1
        alist[position]=currentvalue
    return alist
#print(insertSort([1,22,31,56,66,43,21]))

#谢尔排序
def shellSort(alist):
    sublistcount=len(alist)//2
    while sublistcount>0:
        for startposition in range(sublistcount):
            gapinsertSort(alist,startposition,sublistcount)
        sublistcount//=2
    return alist
def gapinsertSort(alist,start,gap):
    for index in range(start+gap,len(alist),gap):
        currentvalue=alist[index]
        position=index
        while position>=gap and currentvalue<alist[position-gap]:
            alist[position]=alist[position-gap]
            position-=gap
        alist[position]=currentvalue
#print(shellSort([12,21,45,62,28,66]))

#归并排序
def mergeSort(alist):
    if len(alist)>1:
        mid=len(alist)//2
        leftalist=alist[:mid]
        rightalist=alist[mid:]
        mergeSort(leftalist)
        mergeSort(rightalist)
        i=k=j=0
        while i<len(leftalist) and j<len(rightalist):
            if leftalist[i]<rightalist[j]:
                alist[k]=leftalist[i]
                i+=1
            else:
                alist[k]=rightalist[j]
                j+=1
            k+=1
        while i<len(leftalist):
            alist[k]=leftalist[i]
            i+=1
            k+=1
        while j<len(rightalist):
            alist[k]=rightalist[j]
            j+=1
            k+=1
        return alist
#print(mergeSort([11,25,32,18,14,52,37,22]))

#归并排序python特色程序
def merge_Sort(lst):
    if len(lst)<=1:
        return lst
    mid=len(lst)//2
    left=merge_Sort(lst[:mid])
    right=merge_Sort(lst[mid:])
    merge=[]
    while left and right:
        if left[0]<=right[0]:
             merge.append(left.pop(0))
        else:
            merge.append(right.pop(0))
    merge.extend(right if right else left)
    return merge
#print(merge_Sort([12,21,53,11,18,79,86,62]))

#快速排序
def quikSort(alist):
    quikSorthelper(alist,0,len(alist)-1)
    return alist
def quikSorthelper(alist,first,last):
    if first<last:
        splitpoint=partition(alist,first,last)
        quikSorthelper(alist,first,splitpoint-1)
        quikSorthelper(alist,splitpoint+1,last)
def partition(alist,first,last):
    pivotvalue=alist[first]
    leftmark=first+1
    rightmark=last
    done=False
    while not done:
        while leftmark<=rightmark and alist[leftmark]<=pivotvalue:
            leftmark+=1
        while leftmark<=rightmark and alist[rightmark]>=pivotvalue:
            rightmark-=1
        if leftmark>rightmark:
            done=True
        else:
            temp=alist[leftmark]
            alist[leftmark]=alist[rightmark]
            alist[rightmark]=temp
    temp=alist[first]
    alist[first]=alist[rightmark]
    alist[rightmark]=temp
    return rightmark
#print(quikSort([11,21,68,35,67,42,18,98,66,22]))
















