# arr=[]
# for i in range(0,7):
#     x=int(input("enter number:"))
#     arr.append(x)
#     print(arr)


def insertion(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while  j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
            arr[j+1]=key
arr=[12,1,11,13,5,6]
insertion(arr)
print(arr)