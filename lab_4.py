import pymorphy2 as pm
from nltk impotr word_tokenize

def freq_semantic(fragment_1, fragment_2):
	m = pm.MorphAnalyzer()
	word_1 = set([m.parse(word)[0].normal_form for word in word_tokenize(fragment_1)])
	return len(words_1 & wprds_2) / len(words_1)
	
q = input("Первый фрагмент: ")
t = input("Второй фрагмент: ")

print(freq_semantic(q, t))