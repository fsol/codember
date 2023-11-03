"""
Python solution to challenge 1
"""

FILE_PATH = "./data.txt"

with open(FILE_PATH, "r", encoding="utf-8") as data:
    content = data.read()

words = content.split(" ")
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.items():
    print(f"{word}{count}", end="")
