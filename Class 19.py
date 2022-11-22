#def sumdigit(n):
#    sum = 0

#    while n != 0:
#        remainder = n % 10
#        sum += remainder
#        n = n // 10
#        return sum

#n = int(input())
#print(sumDigit(n))

def footToMeter(foot):
    return foot / 0.305
def meterToFoot(meter):
    return meter * 0.305


for i in range(1, 11):
    print(i, footToMeter(i))
for i in range(20, 70, 5):
    print(i, meterToFoot(i))
    