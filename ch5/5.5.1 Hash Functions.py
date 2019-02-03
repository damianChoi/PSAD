def hash(aString, tableSize):
    sum = 0
    for character in aString:
        sum = sum + ord(character)

    return sum % tableSize

def modifiedHash(aString, tableSize):
    sum = 0
    for pos in range(len(aString)):
        sum = sum + pos * ord(aString[pos])

    return sum % tableSize

