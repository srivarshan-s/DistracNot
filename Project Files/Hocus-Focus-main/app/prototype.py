import nltk
from nltk.tokenize import RegexpTokenizer
import speech_recognition as SpeechRecog
import pyaudio
from nltk.corpus import indian
from nltk.tag import tnt
from random_word import RandomWords
import random
from app.hi_rand import hindi_random

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
    is_noun = lambda pos: pos[:2] == 'NN'
    string_filtered = [word for (word, pos) in string_list if is_noun(pos)]
    return string_filtered

def word_filter(string):
    tokenizer = RegexpTokenizer(r'\w+')
    string_list_with_char = tokenizer.tokenize(string)
    string_list = [w for w in string_list_with_char if len(w) > 1]
    def is_noun(pos): return pos[:2] == 'NN'
    nouns = [word for (word, pos) in nltk.pos_tag(string_list) if is_noun(pos)]
    string_filtered = []
    for i in nouns:
        if (nouns.count(i) > 1 and (i not in string_filtered) or nouns.count(i) == 1):
            string_filtered.append(i)
    return string_filtered

def quiz(string,num):
    print(string)
    options=[]
    if int(num) == 1:
        options = RandomWords().get_random_words()[:3]
    else:
        for i in range(3):
            options.append(hindi_random())
    minimize = [words for words in string if len(words) > 5]
    word=random.choice(minimize)
    options.append(word)
    random.shuffle(options)
    return (options,word)

def speech_to_question(num):
    init_rec = SpeechRecog.Recognizer()
    words = []
    for i in range(1):
        with SpeechRecog.Microphone() as source:
            audio_data = init_rec.record(source, duration=5)
            try:text = init_rec.recognize_google(audio_data, language = lang[int(num)])
            except:return (["No","Never","Nope","Yes"],"Yes")
        if int(num) == 1:
            text_filtered = word_filter(text)
        else:
            text_filtered = hi_word_filter(text)
        for j in text_filtered:
            words.append(j)
    return quiz(words,num)
