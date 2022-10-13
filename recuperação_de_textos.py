#Aluno: Thomas Frentzel

#Sua  tarefa  será  transformar  um  conjunto  de  5  sites,  sobre  o  tema  de  processamento  de 
#linguagem natural em um conjunto de cinco listas distintas de sentenças. Ou seja, você fará uma função 
#que, usando a biblioteca Beautifull Soap, faça a requisição de uma url, e extrai todas as sentenças desta 
#url. Duas condições são importantes:  

#a) A página web (url) deve apontar para uma página web em inglês contendo, não menos que 
#1000 palavras.  

#b) O texto desta página deverá ser transformado em um array de senteças.  
 
#Para separar as sentenças você pode usar os sinais de pontuação ou as funções da biblibioteca 
#Spacy. 


import requests
from bs4 import BeautifulSoup


url_1 = requests.get('https://viso.ai/deep-learning/natural-language-processing/')
url_2 = requests.get('https://en.wikipedia.org/wiki/Natural_language_processing')
url_3 = requests.get('https://monkeylearn.com/natural-language-processing/')
url_4 = requests.get('https://www.cio.com/article/228501/natural-language-processing-nlp-explained.html')
url_5 = requests.get('https://levity.ai/blog/how-natural-language-processing-works')



print('1º:')
site1 = BeautifulSoup(url_1.text, "html.parser")
termossite1 = []
for url_1 in site1.find_all("p"):
    termossite1.append(url_1.get_text())

print(termossite1)
print("-------------------------------------------------")


print('2º:')
site2 = BeautifulSoup(url_2.text, "html.parser")
termossite2 = []
for url_2 in site2.find_all("p"):
    termossite2.append(url_2.get_text())

print(termossite2)
print("-------------------------------------------------")


print('3º:')
site3 = BeautifulSoup(url_3.text, "html.parser")
termossite3 = []
for url_3 in site3.find_all("p"):
    termossite3.append(url_3.get_text())

print(termossite3)
print("-------------------------------------------------")


print('4º:')
site4 = BeautifulSoup(url_4.text, "html.parser")
termossite4 = []
for url_4 in site4.find_all("p"):
    termossite4.append(url_4.get_text())

print(termossite4)
print("-------------------------------------------------")


print('5º:')
site5 = BeautifulSoup(url_5.text, "html.parser")
termossite5 = []
for url_5 in site5.find_all("p"):
    termossite5.append(url_5.get_text())

print(termossite5)
print("-------------------------------------------------")
