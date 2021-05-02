import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import indian
from nltk.tag import tnt
import speech_recognition as SpeechRecog
import pyaudio
from random_word import RandomWords
import random
import time
import threading
from hi_rand import hindi_random

init_rec = SpeechRecog.Recognizer()
score = 0
num_ques = 0

lang = {
    1 : 'en-US',
    2 : 'hi-IN'
}

def hi_word_filter(string):
    train_data = indian.tagged_sents('hindi.pos')
    tnt_pos_tagger = tnt.TnT()
    tnt_pos_tagger.train(train_data) #Training the tnt Part of speech tagger with hindi data
    string1=nltk.word_tokenize(string)
    string_list=tnt_pos_tagger.tag(string1)
    # print (string_list)
    is_noun = lambda pos: pos[:2] == 'NN'
    #take only nouns
    string_filtered = [word for (word, pos) in string_list if is_noun(pos)] 
    return string_filtered

def word_filter(string):
    # removes punctuation
    tokenizer = RegexpTokenizer(r'\w+')
    # makes the string into list
    string_list_with_char = tokenizer.tokenize(string)
    # remove single letter
    string_list = [w for w in string_list_with_char if len(w) > 1]
    def is_noun(pos): return pos[:2] == 'NN'
    # take only nouns
    nouns = [word for (word, pos) in nltk.pos_tag(string_list) if is_noun(pos)]
    # remove duplicate
    string_filtered = []
    for i in nouns:
        if (nouns.count(i) > 1 and (i not in string_filtered) or nouns.count(i) == 1):
            string_filtered.append(i)
    return string_filtered


def quiz(string, num):
    global score
    global num_ques
    ran_word = random_words()
    minimize = [words for words in string if len(words) > 5]
    # taking a random word from the correct answer
    random_correct = random.choice(minimize)
    # print(random_correct)
    # appending random word from the wrong answer and correct answer
    options = []
    if num == 1:
        for i in ran_word:
            options.append(i)
    else:
        for i in range(3):
            options.append(hindi_random())
    options.append(random_correct)
    # shuffling all the options
    random.shuffle(options)
    # print(options)
    op1 = options[0]
    op2 = options[1]
    op3 = options[2]
    op4 = options[3]
    print("Choose the word which was mentioned by the professor:")
    print("1.", options[0], "2.", options[1], "3.", options[2], "4.", options[3])
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
        score += 1
        num_ques += 1
    else:
        print("Wrong option")
        num_ques += 1


def random_words():
    r = RandomWords()
    words = r.get_random_words()
    words1 = words[:3]
    return words1


def main(num):
    while True:
        words = []
        for i in range(1):
            with SpeechRecog.Microphone() as source:
                audio_data = init_rec.record(source, duration=20)
                try:
                    text = init_rec.recognize_google(audio_data, language = lang[num])
                except:
                    text = ''
            if num == 1:
                text_filtered = word_filter(text)
            else:
                text_filtered = hi_word_filter(text)
            for j in text_filtered:
                words.append(j)
        quiz(words, num)
        '''
        thread_quiz = threading.Thread(target=quiz, args=(words, ))
        thread_quiz.start()
        thread_quiz.join(timeout=10)
        '''
        print(score)


if __name__ == '__main__':
    main(2)
