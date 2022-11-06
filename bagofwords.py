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

import re
import pandas
import requests
from bs4 import BeautifulSoup

palavras = [] #Para armazenar as sentenças em cinco listas diferentes.
unicos = [] #Para armazenar as sentenças em cinco listas diferentes.
vetor = [] #Aqui é para verificar o numero de vezes que uma palavra aparece em um #determinado arquivo

#urls:
urls = ['https://www.ibm.com/cloud/learn/natural-language-processing', 
        'https://en.wikipedia.org/wiki/Natural_language_processing', 
        'https://monkeylearn.com/natural-language-processing/',
        'https://www.cio.com/article/228501/natural-language-processing-nlp-explained.html',
        'https://magnimindacademy.com/blog/how-do-natural-language-processing-systems-work/']

for site in urls:
    url = requests.get(site).content#guardar o conteudo do site
    soup = BeautifulSoup(url, "html.parser")
    for data in soup(['style', 'script']):#remover os scripts e estilos
        data.decompose()#remover os scripts e estilos
    palavra = ' '.join(soup.stripped_strings)
    palavra = re.sub(r"[\n\t]", "", palavra)#remover os espaços em branco
    separadores = re.split("[!?.;:,]", palavra)#separar as sentenças
    palavras.append(" ".join(separadores))#adicionar as sentenças em uma lista

def unico(p): #verificar se a palavra já existe no vetor
  sem_rep = set() #criar um conjunto vazio
  for array in p: #percorrer o vetor
    for palavra in array.split(): #percorrer cada palavra do vetor
        sem_rep.add(palavra) #adicionar a palavra no conjunto
  return sem_rep #retornar o conjunto

unicos = unico(palavras) #chamar a função unico
unicos = list(unicos) #transformar o conjunto em lista para poder usar o index
print(len(unicos)) #imprimir o tamanho do vetor

def BOW(arrayDePalavras, texto): #função para gerar a matriz termo documento
  array = [0] * len(arrayDePalavras)  #criar um vetor com o tamanho do vetor de palavras
  for string in texto.split(): #percorrer cada palavra do texto
    array[arrayDePalavras.index(string)] += 1 #adicionar 1 no vetor na posição da palavra
  return array #retornar o vetor

for array in palavras: #percorrer cada sentença
    vetor.append(BOW(unicos, array)) #chamar a função BOW e adicionar o vetor na lista

df = pandas.DataFrame(vetor, columns=unicos) #criar um dataframe com o vetor e as palavras
display(df) #imprimir o dataframe
