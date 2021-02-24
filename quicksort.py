def quick(seq):
    n=len(seq)

    if n<=1:
        return seq
    else:
        pivot=seq.pop()
    
    greater=[]
    lower=[]
    for i in seq:
        if pivot > i:
            greater.append(i)
        else:
            lower.append(i)
    return quick(greater)+[pivot]+quick(lower)
print(quick([5,6,7,8,3,4,2,90,23]))