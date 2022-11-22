import random
chars = []
num = 100
for i in range(100):
    char = random.randint(ord('a'), ord('z'))
    chars.append(chr(char))
count = [] #[0] * 26 also works
for i in range(26):
    count.append(0)
for c in chars:
    count[ord(c) - ord('a')] += 1
print(count)
