def linearProbing(items, slotSize):
    hashTable = [None] * slotSize
    for item in items:
        slot = item % slotSize
        while hashTable[slot] != None:
            slot = slot + 1
        hashTable[slot] = item

    return hashTable

print(linearProbing([113, 117, 97, 100, 114, 108, 116, 105, 99], 11))

