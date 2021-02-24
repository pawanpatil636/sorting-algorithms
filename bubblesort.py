
#---------------------------BUBBLE SORTING ALGORITHM------------------------------


def bubbleSort(array):
    n=len(array)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                array[j] , array[j+1]= array[j+1],array[j] 
array=[56,79,2,34,00,13,52]
bubbleSort(array)
# for i in range(len(array)):
print(array,end=" ")