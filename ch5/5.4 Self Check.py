
def recursiveBinarySearchV2(alist, item, first=None, last=None):

    if first == None:
        first = 0
    if last == None:
        last = len(alist) - 1
    if first > last:
        return False

    else:
        midpoint = (first+last) // 2
        if alist[midpoint] == item:
            return True
        elif alist[midpoint] > item:
            return recursiveBinarySearchV2(alist, item, first, midpoint-1)
        else:
            return recursiveBinarySearchV2(alist, item, midpoint+1, last)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(recursiveBinarySearchV2(testlist, 3))
print(recursiveBinarySearchV2(testlist, 13))

