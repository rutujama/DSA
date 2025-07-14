def merge_sort(list1):
    if len(list1)>1:
        mid=len(list1)//2
        leftside=list1[:mid]
        rightside=list1[mid:]
        merge_sort(leftside)
        merge_sort(rightside)
        i=j=k=0
        while i<len(leftside) and j<len(rightside):
            if leftside[i]<rightside[j]:
                list1[k]=leftside[i]
                i+=1
            else:
                list1[k]=rightside[j]
                j+=1
            k+=1
        while i<len(leftside):
            list1[k]=leftside[i]
            i+=1
            k+=1
        while j<len(rightside):
            list1[k]=rightside[j]
            j+=1
            k+=1
l=[43,54,67,89,671,9]
merge_sort(l)
print(l)               
                        