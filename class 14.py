import random
list1 = []
num = 1000
for i in range(100):
    list1.append(random.randint(0, 100))

avg = sum(list1) / len(list1)
count = 0
for x in list1:
    if x > avg:
        count += 1
len([x for x in list1 if x > avg])
