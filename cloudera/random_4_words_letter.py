# -*- coding: utf-8 -*-
# random_4_words_letter.py

import random

with open('/Users/yunpengli/PycharmProjects/yaamnotes/cloudera/interview_preparation.py', 'r') as f:
    words = f.read()

print(words)
word = random.choice(words.split())
print("---------"*5)
print(word)
letter = []
count = 4
while count > 0:
    letter.append(random.choice(words.split()))
    count -= 1

print(letter)
print(' '.join(letter))
