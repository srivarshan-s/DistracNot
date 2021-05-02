import nltk
from nltk.tokenize import RegexpTokenizer

def word_filter(string):
    #removes punctuation
    tokenizer = RegexpTokenizer(r'\w+')

    #makes the string into list
    string_list_with_char=tokenizer.tokenize(string)

    #remove single letter
    string_list=[w for w in string_list_with_char if len(w)>1]

    is_noun = lambda pos: pos[:2] == 'NN'

    #take only nouns
    nouns = [word for (word, pos) in nltk.pos_tag(string_list) if is_noun(pos)]

    #remove duplicate
    string_filtered=[]
    for i in nouns:
        if (nouns.count(i)>1 and (i not in string_filtered) or nouns.count(i)==1):
            string_filtered.append(i)

    return string_filtered