import random

words_list = []

while True:
    word = input("Bitte gib ein Wort ein (q zum Beenden): ")
    
    if word == "q":
        break

    words_list.append(word)

words_list.sort(reverse=True)


print("Sortierte Liste:")
print(words_list)
