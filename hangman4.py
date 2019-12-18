import random

print("H A N G M A N")
word = ['python', 'java', 'kotlin', 'javascript']

def listToString(l):
    strWord = ''
    for i in l:
        strWord += i
    return  strWord

word_random = random.choice(word)
wordTolist = list(word_random)

maskedWord = len(word_random)*'-'
print(maskedWord)

for i in range(8):
    print('Input a letter:')
    x = input()
    maskedWord = list(maskedWord)
    for j in range(len(wordTolist)):
        if x == wordTolist[j]:
            maskedWord[j] = x

    if x not in wordTolist:
        print("No such letter in the word")

    print(listToString(maskedWord))


print('Thanks for playing!')
print("We'll see how well you did in the next stage")

#csdacacascavsavsvsvsvsdvsv
#test 2 must branch