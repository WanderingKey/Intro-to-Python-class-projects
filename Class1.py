s = input()
countVowels = 0
countConsonants = 0
for c in s:
    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
        countVowels += 1
    elif c.isalpha():
        countConsonants += 1
print(countVowels, countConsonants)