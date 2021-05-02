from words import keyword_filter
from api import random_words
import random


def quiz(string):
    ran_word = random_words()

    minimize = [words for words in string if len(words) > 5]

    # taking a random word from the correct answer
    random_correct = random.choice(minimize)
    # print(random_correct)

    # appending random word from the wrong answer and correct answer
    options = []
    for i in ran_word:
        options.append(i)
    options.append(random_correct)

    # shuffling all the options
    random.shuffle(options)
    # print(options)

    op1 = options[0]
    op2 = options[1]
    op3 = options[2]
    op4 = options[3]

    print("Choose the word which was mentioned by the professor:")
    print("1.", op1, "2.", op2, "3.", op3, "4.", op4)
    user_choice = input("Enter option:")
    if user_choice == "1":
        ans = op1
    elif user_choice == "2":
        ans = op2
    elif user_choice == "3":
        ans = op3
    elif user_choice == "4":
        ans = op4
    else:
        print("Inavlid option")

    if ans == random_correct:
        print("Correct option")
    else:
        print("Wrong option")
