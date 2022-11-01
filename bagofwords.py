#Thomas Frentzel

# Sua tarefa será  gerar a matriz termo documento, dos documentos recuperados da internet e 
# imprimir esta matriz na tela. Para tanto: 
#   a) Considere que todas as listas de sentenças devem ser transformadas em listas de vetores, 
# onde cada item será uma das palavras da sentença. 
#   b) Todos  os  vetores  devem  ser  unidos  em  um  corpus  único  formando  uma  lista  de  vetores, 
# onde cada item será um lexema.  
#   c) Este único corpus será usado para gerar o vocabulário. 
#   d) O  resultado  esperado  será  uma  matriz  termo  documento  criada  a  partir  da  aplicação  da 
# técnica bag of Words em todo o corpus.  

from bs4 import BeautifulSoup
import requests
import spacy

spa = spacy.load("en_core_web_sm")

# 1º url e suas funções:

url_1 = requests.get('https://www.ibm.com/cloud/learn/natural-language-processing')

site1 = BeautifulSoup(url_1.text, "html.parser")

st1 = BeautifulSoup(url_1.text,"html.parser").find("p").get_text()

# 2º url e suas funções:

url_2 = requests.get('https://en.wikipedia.org/wiki/Natural_language_processing')

site2 = BeautifulSoup(url_2.text, "html.parser")

st2 = BeautifulSoup(url_2.text,"html.parser").find("p").get_text()

# 3º url e suas funções:

url_3 = requests.get('https://monkeylearn.com/natural-language-processing/')

site3 = BeautifulSoup(url_3.text, "html.parser")

st3 = BeautifulSoup(url_3.text,"html.parser").find("p").get_text()

# 4º url e suas funções:

url_4 = requests.get('https://www.cio.com/article/228501/natural-language-processing-nlp-explained.html')

site4 = BeautifulSoup(url_4.text, "html.parser")

st4 = BeautifulSoup(url_4.text,"html.parser").find("p").get_text()

# 5º url e suas funções:

url_5 = requests.get('https://magnimindacademy.com/blog/how-do-natural-language-processing-systems-work/')

site5 = BeautifulSoup(url_5.text, "html.parser")

st5 = BeautifulSoup(url_5.text,"html.parser").find("p").get_text()


#Para armazenar as sentensas em cinco listas diferentes.

def unico(p):
  n = spa(p)
  return [n.orth_ for n in n if not n.is_punct]

sent_site1 = unico(st1)
sent_site2 = unico(st2)
sent_site3 = unico(st3)
sent_site4 = unico(st4)
sent_site5 = unico(st5)

#um vocabulario com todas as palavras dos cinco arquivos

Vcb = (sent_site1 + sent_site2 + sent_site3 + sent_site4 + sent_site5)
vetor = [Vcb]

snt_vetor = []

#Aqui é para verificar o numero de vezes que uma palavra aparece em um
#determinado arquivo

def BOW(sent, Vcb):
  VetP = []
  for palavra in Vcb:
    freq = 0
    for sent in sent:
      if sent == palavra:
        freq += 1
    VetP.append(freq)
  return VetP

#Armazena tudo dentro de um vetor.
vetor.append(BOW(sent_site1, Vcb))
vetor.append(BOW(sent_site2, Vcb))
vetor.append(BOW(sent_site3, Vcb))
vetor.append(BOW(sent_site4, Vcb))
vetor.append(BOW(sent_site5, Vcb))

#Prints
print("Palavras extraidas dos sites: ",Vcb)
print("------------------------------------------------")
print("Quantidade de vezes que as palavras se repetem no site 1: ",vetor[1])
print("------------------------------------------------")
print("Quantidade de vezes que as palavras se repetem no site 2: ",vetor[2]) 
print("------------------------------------------------")
print("Quantidade de vezes que as palavras se repetem no site 3: ",vetor[3]) 
print("------------------------------------------------")
print("Quantidade de vezes que as palavras se repetem no site 4: ",vetor[4])
print("------------------------------------------------") 
print("Quantidade de vezes que as palavras se repetem no site 5: ",vetor[5])

