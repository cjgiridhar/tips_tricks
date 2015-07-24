__author__ = 'cgiridhar'

class Sort:

    def __init__(self, array):
        self.array = array

    def __swap(self, a,b, arr):
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp

    def bubbleSort(self):
        """Bubble Sort Implementation"""
        arr = self.array
        n = len(arr)
        for m in reversed(range(n)):
            for i in range(n-1):
                if arr[i] < arr[i+1]:
                    pass
                else:
                    self.__swap(i, i+1, arr)
        return arr


    def selectionSort(self):
        """Selection Sort Implementation"""
        arr = self.array
        n = len(arr)
        for i in range(n):
            index = i
            for j in range(i+1,n):
                if arr[j] < arr[index]:
                    index = j
            self.__swap(index, i, arr)
        return arr


array = [8,4,66,7,88,8,99]
s = Sort(array)
# print s.bubbleSort()
print s.selectionSort()