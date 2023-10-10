def char_count(str):
  pairsDict = {}

  for char in str:
    if char in pairsDict:
      pairsDict[char] += 1
    else:
      pairsDict[char] = 1

  countLst = []
  #for key, values in pairsDict

  return pairsDict
  

print(char_count("aaabbc"))
