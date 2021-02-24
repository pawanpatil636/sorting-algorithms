#----------------------------selection sort---------------------------------------
a=[]
for i in range(0,5):
    q=int(input("the input is :"))
    a.append(q)
    print(a)
    for i in range(len(a)):
        min_index=i
        for j in range(i+1, len(a)):
            if a[min_index]>a[j]:
                min_index=j
                a[i],a[min_index]=a[min_index],a[i]
print( "sorted array is :",a)
