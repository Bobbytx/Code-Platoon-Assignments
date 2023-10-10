def sum_pairs(numberList, desiredSum):
    resultLst = []
    numPairs = 0
    for n1 in range(len(numberList)):
        for n2 in range(n1+1, len(numberList)):
            numPairs = numberList[n1] + numberList[n2]
            if numPairs == desiredSum:
                numLst = [numberList[n1], numberList[n2]]
                resultLst.append(numLst)
    return resultLst


print(sum_pairs([1,2,3,4,5], 7))