# 5.5 Hashing

def hashFunction(item):
    return item % 11

def hashTableGenerator(itemList):
    hashTable = [None] * 11
    for item in itemList:
        slot = hashFunction(item)
        hashTable[slot] = item
    return hashTable

def findInHashTable(item, hashTable):
    slot = hashFunction(item)
    return hashTable[slot] == item

def main():
    itemList = [54, 26, 93, 17, 77, 31]
    hashTable = hashTableGenerator(itemList)
    print(findInHashTable(54, hashTable))

main()