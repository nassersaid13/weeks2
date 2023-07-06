def isPair(number):
    return number%2 == 0

def calculateOddNumbersByRange(min,max): 
    print("Calculating pair numbers")
    numbers = range(min,max) 
    for number in numbers:
        if isPair(number):
            print(number)

def calculatePairNumbersByRange(min,max):
    print("Calculating odd numbers")
    numbers = range(min,max) 
    for number in numbers:
        if not isPair(number):
            print(number)

def calculateSum(numbers):
    print("Calculating sum")
    amount = 0
    for number in numbers:
        amount += number
    print(amount)
      
#max = int(input("Number:"))
#calculateOddNumbersByRange(1,max)
numbers = range(1,5)
calculateSum(numbers)