__author__ = 'cgiridhar'

class Search:
    def __init__(self, array):
        self.array = array

    def linearSearch(self, key):
        for i in self.array:
            if key == i:
                return key
            else:
                pass
        return -1

    def binarySearch(self, key):
        start = 0
        end = len(self.array)
        while start <= end:
            mid = (end + start)/2
            print "Mid is:", mid
            if self.array[mid] == key:
                return mid
            if key < self.array[mid]:
                end = mid - 1
            else:
                start = mid + 1


s = Search([2,55,66,77,222])
print s.binarySearch(55)