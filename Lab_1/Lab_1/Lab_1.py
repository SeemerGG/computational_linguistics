from nltk import *
from nltk.corpus import stopwords
import docx 
import string


def input_doxc():
    data_docx = docx.Document('input.docx')
    data = []
    for paragraph in data_docx.paragraphs:
        data.append(paragraph.text)
    data = ' '.join(data)
    return data

def graphematic_analiz(data):
    
    list_sent = sent_tokenize(data) #—писок предложений

    data_without_znaks = data.lower()
    for s in string.punctuation:
        if s in data_without_znaks:
            data_without_znaks = data_without_znaks.replace(s,'') #—трока без знаков препинани€ 
    list_words = word_tokenize(data_without_znaks)
    download('stopwords')
    list_stop_word = set(stopwords.words('russian'))
    list_words = [i for i in list_words if i not in list_stop_word]
    #list_words - список без стоп слов и знаков + все в нижнем регистре

    #—оздаю словарь где ключем €вл€етс€ частота встречаемости слова
    dict_frequency = {}
    for i in list_words:
        if i in dict_frequency:
            dict_frequency[i] = dict_frequency[i]+1
        else:
            dict_frequency[i] = 1
    return [list_sent, list_words, dict(sorted(dict_frequency.items(), key = lambda x: x[1], reverse = True))]

graph_analiz = graphematic_analiz(input_doxc())

print(graph_analiz[0])
print("\n")
print(graph_analiz[1])
print('\n')
print(graph_analiz[2])

