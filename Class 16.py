
#l = s.split()
#l2 = [int(x) for ix in l]
#l2.reverse()
#print(l2)

s = input()
l = s.split()
l = [int(x) for x in l]
limit = 100
counts = [0] * limit
counts = []
for n in l:
    if n > 0 and n <= limit:
        counts[n - 1] += 1
for i in range(limit):
    if counts[i] > 0:

