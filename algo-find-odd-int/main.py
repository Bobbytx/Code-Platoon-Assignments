def find_it(seq):
    resultDict = {}
    if len(seq) == 1:
        return seq[0]

    for num in seq:
        if num in resultDict:
            resultDict[num] += 1
        else:
            resultDict[num] = 1

    for num in resultDict:
        if resultDict[num] % 2 != 0:
             return num
        
print(find_it([1,1,2,2,0,0,0]))
