def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        elif alist[midpoint] > item:
            last = midpoint - 1
        else:
            first = midpoint + 1

    return found



def recursiveBinarySearch(alist, item):
    if len(alist) ==  0:
        return False

    else:
        midpoint = len(alist) // 2

        if alist[midpoint] == item:
            return True
        elif alist[midpoint] < item:
            return recursiveBinarySearch(alist[midpoint+1:], item)
        else:
            return recursiveBinarySearch(alist[: midpoint], item)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(recursiveBinarySearch(testlist, 3))
print(recursiveBinarySearch(testlist, 13))