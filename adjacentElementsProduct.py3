def adjacentElementsProduct(inputArray):
    result = []
    for i in range(len(inputArray)-1):
        result.append(inputArray[i]*inputArray[i+1])
    return max(result)
