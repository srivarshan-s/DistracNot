from random_word import RandomWords

def random_words():
	r = RandomWords()
	words=r.get_random_words()
	words1=words[:3]
	return words1
