def insertion_sort(list1):
    for i in range(1,len(list1)):
        temp=list1[i]
        j=i-1
        while j>=0 and temp<list1[j]:
            list1[j+1]=list1[j]
            j-=1
        list1[j+1]=temp
l=[32,67,450,122,135,69]
insertion_sort(l)
print(l)            



            