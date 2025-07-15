def quick_sort(list1):
    if len(list1)<1:
        return list1
    else:
        pivot=list1[0]
        lesser=[x for x in list1[1:] if x<=pivot]
        greater=[x for x in list1[1:] if x>pivot]
        return quick_sort(lesser)+[pivot]+quick_sort(greater)
l=[32,56,78,52,67]
l=quick_sort(l)
print(l)    