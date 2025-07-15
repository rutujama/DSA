def bubble_sort(list1):
    flag=False
    for i in range(1,len(list1)):
        flag=False
        for r in range(len(list1)-i):
            if list1[r]>list1[r+1]:
                list1[r],list1[r+1]=list1[r+1],list1[r]
                flag=True
        if not flag:
            break
l=[667,78,45,304,67,10]
bubble_sort(l)
print(l)                
        