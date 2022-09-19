from nltk import *
from nltk.corpus import stopwords
import docx 

#вывод из файла .docx
data_docx = docx.Document('input.docx')

#считывание данных из файла в data
data = []

for paragraph in data_docx.paragraphs:
    data.append(paragraph.text)
data = ' '.join(data)


##Пример 1. разделение входного текста на предложения 

#sent = sent_tokenize(data)
#print(sent)

##Пример 2. Разделение текста на слова 

#sent2 = word_tokenize(data)

#print (sent2)

##Пример 3. Скачивание списка стоп слов (был произведен в консоли отдельно)
##from nltk import download
##download('stopwords')

##Пример 4. Просмотр стоп-слов

#print(stopwords.words('russian'))

##Пример 5.Удаление стоп-слов из предложения 


#stop_words = set(stopwords.words('russian'))
#sent2_without_stop_words = [word for word in sent2 if not word in stop_words]

#print(sent2_without_stop_words)

#Разработка графематического анализатора

sent = sent_tokenize(data)
