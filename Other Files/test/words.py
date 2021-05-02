import nltk
from nltk.tokenize import RegexpTokenizer
    
#str1="The official mammal class is Mammalia. Animals that are considered mammals include warm-blooded vertebrates that have hair or fur and whose babies drink milk. Unlike other animal types like birds and insects, all mammal babies drink milk that comes from their mother’s bodies. This is one of the key ways to know if an animal is a mammal."
#print(str1)

def keyword_filter(string):
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

