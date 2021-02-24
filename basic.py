class stack():
    def __init__(self,maxlength):
        self.maxlength=maxlength
        self.arr=[]
    def isfull(self):
        if len(self.arr)==self.maxlength:
            return True
        return False

    def isempty(self):
        if len(self.arr)==0:
            return True
        return False

    def push(self,num):
        if self.isfull()==True:
            print("array is full cannot push") 
        else:
            self.arr.append(num)

    def pop(self):
        if self.isempty()==True:
            print("array is empty cannot remove")
        else:
            return self.arr.pop()

    def show_data(self):
        if self.isempty()==True:
            print("no data present")
            return
        else:
            for i in self.arr:
                print(i)

    def peak(self,index):
        if self.isempty()==True:
            print("empty ")
        else:
          print(self.arr[index])

    def bubbleSort(self):
        n = len(self.arr)
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if self.arr[j] > self.arr[j+1] :
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
                    print(self.arr)
                    swapped = True
                    if swapped == False:
                        break
