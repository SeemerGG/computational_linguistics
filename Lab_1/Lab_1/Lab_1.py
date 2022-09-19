from nltk import *
from nltk.corpus import stopwords
import docx 

#����� �� ����� .docx
data_docx = docx.Document('input.docx')

#���������� ������ �� ����� � data
data = []

for paragraph in data_docx.paragraphs:
    data.append(paragraph.text)
data = ' '.join(data)


##������ 1. ���������� �������� ������ �� ����������� 

#sent = sent_tokenize(data)
#print(sent)

##������ 2. ���������� ������ �� ����� 

#sent2 = word_tokenize(data)

#print (sent2)

##������ 3. ���������� ������ ���� ���� (��� ���������� � ������� ��������)
##from nltk import download
##download('stopwords')

##������ 4. �������� ����-����

#print(stopwords.words('russian'))

##������ 5.�������� ����-���� �� ����������� 


#stop_words = set(stopwords.words('russian'))
#sent2_without_stop_words = [word for word in sent2 if not word in stop_words]

#print(sent2_without_stop_words)

#���������� ���������������� �����������

sent = sent_tokenize(data)
