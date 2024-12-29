import os
import random
import string

def random_letters():
    letters = [random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(9)]
    return letters

def find_words():
    words = set()
    with open('words.txt') as file:
        for line in file:
            word = line.strip().upper()
            if len(word) == 9:
                words.add(word)
    word = random.choice(list(words))
    letters = list(word)
    random.shuffle(letters)
    return letters

while True:
    os.system("clear")
    version = input("1. Random 9 letters \n2. 9 letters can made up a word \nEnter 1 or 2: ")
    if version == '1':
        letters = random_letters()
        break
    elif version == '2':
        letters = find_words()
        break
    else: 
        continue


correct = ''
points = 0
words = set()
answers = []

with open('words.txt') as file:
    for line in file:
        word = line.strip().upper()
        words.add(word)

foundWords = set()
for word in words:
    if set(word).issubset(set(letters)) and all(word.count(letter) <= letters.count(letter) for letter in set(word)):
        foundWords.add(word)

while True:
    os.system("clear")
    print(letters)
    print(f"Total points: {points}")
    print(correct)
    word2 = input("Enter a word (Enter 1 to end of game): ")
    if word2.upper() == '1':
        break
    elif word2.upper() in answers:
        correct = 'Word is already used.'
    elif word2.upper() not in foundWords:
        correct = 'Wrong'
    elif word2.upper() in foundWords:
        points += len(word2)
        foundWords.remove(word2.upper())
        answers.append(word2.upper())
        correct = 'Correct'

print(f'Your answers: {answers}')
print(f'Other possible answers: {foundWords}')
print()

username = input("Enter your username: ")
print()
scores = []
with open("highscores.txt") as f:
    for line in f:
        name, score = line.strip().split(": ")
        scores.append((name, int(score)))
scores.append((username, points))
scores.sort(key=lambda x: x[1], reverse=True)
scores = scores[:10]

with open("highscores.txt", "w") as f:
    for name, score in scores:
        f.write(f"{name}: {score}\n")

for i, (name, score) in enumerate(scores):
    print(f"{i+1}. {name}: {score}")

ranking = -1
for i, (name, score) in enumerate(scores):
    if name == username and score == points:
        ranking = i + 1
        break

print(f"Your total score: {points}")
if ranking > 0 and ranking <= 10:
    print(f"Congratulations! You are in {ranking} place.")
else:
    print("You did your best!")
