import random
import re

word = ['pythona', 'java', 'kotlina', 'javascript']
corect_answer = random.choice(word)
masked_word = len(corect_answer)*'-'
message = 'Input a letter: '

print("H A N G M A N")

for i in range(8):
    print(masked_word)
    user_answer = input(message)

    founded = [m.start() for m in re.finditer(user_answer, corect_answer)]
    if len(founded) == 0 or len(founded) == len(founded):
        print("No such letter in the word")
    else:
        for x in founded:
            masked_word = masked_word[:x] + user_answer + masked_word[x + 1]
        print(founded)

print('Thanks for playing!')
print("We'll see how well you did in the next stage")


