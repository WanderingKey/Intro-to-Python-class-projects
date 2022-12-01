#i = list(range(0,1000,9)) 
#print (i) 
#i = len(i) 
#print (i)
#import random  different code
#counts = []
#for i in range(10):
#    counts.append(0)
#for i in range(1000):
#    n = random.randint(0, 9)
#    counts[n] += 1

#print(counts)

def indexOfSmallestElement(lst):
    smallest = lst[0]
    for i in range(1, len(lst)):
        if smallest > lst[i]:
            index = i 
            smallest = lst[i]
    return index
s = input()
l = s.split()
print(indexOfSmallestElement(l))