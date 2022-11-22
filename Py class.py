number = int(input())
countpositive = 0
countnegative = 0
total = 0

while number !=0:
    if number > 0:
        countpositive += 1
    elif number < 0:
        countnegative += 1
    total += number

avg = total / (countpositive + countnegative)
print(countpositive, countnegative)
print(total, avg)