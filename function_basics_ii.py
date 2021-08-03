# Countdown

def countdown(num):
    countdownList = []
    for x in range(num, -1, -1):
        countdownList.append(x)
    return countdownList

print(countdown(5))

# Print and Return

def printAndReturn(printValue, returnValue):
    print(printValue)
    return returnValue

print(printAndReturn(1, 2))

# First Plus Length

def firstPlusLength(list):
    length = len(list)
    return (list[0] + length)

print(firstPlusLength([17,2,3,4,7]))

# Values Greater than Second

def greaterThan(list):
    total = 0
    newList = []
    for x in range(0, len(list)):
        if (len(list) == 1):
            return False
        if (list[x] > list[1]):
            newList.append(list[x])
            total += 1
    print(total)
    return newList

print(greaterThan([5,2,3,2,1,4]))
print(greaterThan([3]))
print(greaterThan([5,500,3,2,1,4]))

# This Length, That Value

def lengthAndValue(length, value):
    singleList = []
    for x in range(0,length):
        singleList.append(value)
    return singleList

print(lengthAndValue(4, 7))
print(lengthAndValue(6, 2))