def calculateAverage(number1, number2, number3):
    average = (number1 + number2 + number3) / 3
    return  average


def calculateAverageNoReturn(number1, number2, number3):
    average = (number1 + number2 + number3) / 3

    if (average == 10):
        return

    return  average


def returnMoreThanOneValue(number1, number2):
    number1 += 100
    number2 += 200
    return number1, number2


value = calculateAverage(10,10,10)

print(value)

value1 , value2  = returnMoreThanOneValue(100,2500)




