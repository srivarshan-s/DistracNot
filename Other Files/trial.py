import speech_recognition as SpeechRecog
import pyaudio
from random_word import RandomWords
import random
import time
import threading

init_rec = SpeechRecog.Recognizer()
score = 0
num_ques = 0

lang = {
    1: 'en-US',
    2: 'hi-IN',
    3: 'ta-IN',
    4: 'te-IN',
    5: 'kn-IN',
    6: 'zh-CN',
    7: 'ja-JP',
    8: 'it-IT',
    9: 'fr-FR',
    10: 'de-DE'
}

def quiz(string):
    global score
    global num_ques
    ran_word = random_words()
    # taking a random word from the correct answer
    random_correct = []
    minimize = [words for words in string if len(words) >= 5]
    len_str = len(minimize)
    x = random.randint(0, len_str)
    for i in range(3):
        random_correct.append(minimize[(x+i)%len_str])
    random_correct = ' '.join(random_correct)
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
    print("1.", options[0], "2.", options[1],
          "3.", options[2], "4.", options[3])
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
    word_final = []
    words1 = words[:3]
    words1 = ' '.join(words1)
    word_final.append(words1)
    words2 = words[3:6]
    words2 = ' '.join(words2)
    word_final.append(words2)
    words3 = words[6:9]
    words3 = ' '.join(words3)
    word_final.append(words3) 
    return word_final


def main(num):
    while True:
        words = []
        for i in range(1):
            with SpeechRecog.Microphone() as source:
                audio_data = init_rec.record(source, duration=10)
                try:
                    text = init_rec.recognize_google(audio_data, language = lang[num])
                except:
                    text = ''
        #text = 'Note that we may get different output because this program generates random number in range 0 and 9.'
        text_filtered = text.split(' ')
        for j in text_filtered:
            words.append(j)
        quiz(words)
        '''
        thread_quiz = threading.Thread(target=quiz, args=(words, ))
        thread_quiz.start()
        thread_quiz.join()
        '''
        print(score)


if __name__ == '__main__':
    main(3)
