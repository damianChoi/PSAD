def recDC(coinValueList,change,knownResults):
   minCoins = change
   if change in coinValueList:
      knownResults[change] = 1
      print(change, knownResults)
      return 1
   elif knownResults[change] > 0:
      print(change, knownResults)
      return knownResults[change]
   else:
      for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recDC(coinValueList, change-i,
                              knownResults)
         if numCoins < minCoins:
            minCoins = numCoins
            knownResults[change] = minCoins
   print(change, knownResults)
   return minCoins

print(recDC([1,5,10,25],63,[0]*64))
