def getAvg(num1, num2):
    result = (num1 +num2) / 2
    return result
def getTotal(num1, num2):
    result = num1 +num2
    return result

def main():
    num1 = input()
    num2 = input()
    print(getTotal(num1, num2), getAvg(num1, num2))