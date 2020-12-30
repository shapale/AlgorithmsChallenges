def twoNumberSum(array, targetNum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i+1,len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetNum:
                return [firstNum,secondNum]
    return []