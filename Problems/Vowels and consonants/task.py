vowel = ['a', 'e', 'i', 'o', 'u']
word = list(input())

for i in word:
    if i in vowel:
        print("vowel")
    elif i.isalpha():
        print("consonant")
    else:
        break
