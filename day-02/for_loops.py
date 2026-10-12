word = input("Enter a word: ")

vowels = 0
consonants = 0

for ch in word:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1

print("Total vowels:", vowels)
print("Total consonants:", consonants)
