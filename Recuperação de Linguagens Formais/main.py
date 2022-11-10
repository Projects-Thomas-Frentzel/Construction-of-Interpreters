#Thomas Frentzel
'''Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  fazer  um  programa,  usando  a 
linguagem de programação Python, C++, C, que seja capaz de validar e executar programas escritos na 
linguagem  proposta  a  seguir  emitindo  um  relatório  de  análise  léxica,  a  classificação  como  válida  ou 
invalida para cada declaração da linguagem e o resultado do programa.   
Descrição da linguagem  
Identificadores: compostos apenas de letras minúsculas e números;  
Símbolos especiais: ?, ), (;  
Operações:  soma  (+),  subtração  (-),  multiplicação  (*),  divisão  (/),  seno  (sin),  cosseno  (cos), 
exponenciação (exp), raiz (rot) segundo os seguintes exemplos:  
(3 4 +) representa a soma de 3 e 4 e devolve 7.000;  
  (3.4 2.5 -) representa a subtração entre 3,6 e 2,5 e devolve 1.100;  
(2.5 3 *) representa o produto de 2,5 por 3 e devolve 7.500;   
(2.6 2 /) representa a divisão de 2,6 por 2 e devolve 1.300;  
   (sin 30) representa o seno de 30 graus e devolve 0.500;  
   (cos 30) representa o cosseno de 30 graus e devolve 0.866;  
   (exp 3 2) representa 3 elevado a 2 e devolve 9.000;  
   (rot 81 2) representa a raiz quadrada de 81 e devolve 9.000;  
Observe  que  todos  os  números  são  reais  de  precisão  dupla  e  todos  os  resultados  serão 
truncados na terceira casa depois da vírgula.  
O símbolo especial será usado para passar o resultado de uma linha para a linha seguinte. Assim, 
um arquivo contendo as declarações a seguir:   
(3 4 +)  
(2 ? *)  
Deverá  devolver  como  reposta  14  além da  validação  de todos  os  lexemas  e da  validação  das 
declarações. Para o exemplo acima, a saída deverá ser:   
Linha 1: lexemas: (, 3, 4, +,) todos válidos  
Linha 1: sintaxe: correta  
Linha 2: lexemas: (, 2, ?, ) todos válidos  
Linha 2: sintaxe: correta  
Além  disso,  poderemos  usar  indentificadores  e  ainhamento.  Então  para  criar  uma  variável  e 
armazenar um valor usaremos a sentença:   
  
(teste (2 3 *))   
Neste exemplo foi criada a variável teste e esta variável irá armazenar o valor 6.000.   
Um programa completo poderia ser escrito como:   
  
(op1 15)  
(op2 2)  
(sin (op1 op2 *) ) 
(3 ? *)  
Neste exemplo o resultado será 1.500.  
Considerações  importantes:  para  testar  seu  programa,  você  deverá  enviar  três  arquivos 
contendo  programas  com  6  ou  mais  declarações  que  usem  todas  as  operações  descritas  com  pelo 
menos dois aninhamento de operações em cada arquivo de testes e com, no mínimo uma variável em 
cada arquivo de testes.   
Os testes devem ser capazes de indicar o comportamento do seu programa caso o código criado 
contenha erros léxicos ou sintáticos.  
Para a realização da validação léxica você deverá simular, em código, uma máquina de estados 
finitos e não poderá utilizar nenhuma expressão regular.   
Para  a  realização  da  validação  sintática  você  pode  usar  um  parser  LL1  ou  criar  o  seu  próprio 
código de validação de declarações. '''

import string
import math

alfa_valid = string.ascii_lowercase

def get_file(file):
  return open(file).read()

counterwhile = 0 
      
while counterwhile < 3:
  listapronta = []
  counterwhile = counterwhile + 1
  opcaocontagem = []
  file = get_file(f"teste{counterwhile}.txt").split("\n")
  validadorparenteses = False
  verificar = []
  
  for i in file:
    verificar.append("1")
    a = i.split(" ")
    novo = []
    listcountleft = 0
    for m in a:
      for n in m:
        x = "("
        xe = ")"
        if n == x:
          listcountleft = listcountleft + 1
    listcountrigjt = 0
    validadornumerolistas = False
    for l in a:
      for t in l:
        for o in t:
          if o == '1' or o == '2' or o == '3' or o == '4' or o == '5' or o == '6' or o == '7' or o == '8' or o == '9':
            validadornumerolistas = True

        
    for m in a:
      for n in m:
        x = "("
        xe = ")"
        if n == xe:
          listcountrigjt = listcountrigjt + 1
    if listcountrigjt == listcountleft:
      print(" ")
    else:
      print(" ")
      validadorparenteses = True
    for x in a:
      item = x
      for y in ['\n', '\t', '(', ')']:
        item = item.replace(y, "")
      novo.append(item)
    a = novo
    removerInterrog = False
    for interrog in a:
      if interrog == '?':
        removerInterrog = True
    listaprontaB = []


        
    a = [ x for x in a if x != '?' ]
    
      
    bufferopcaocontagem = False
    verificaroperacao = False
    
    for q in a:
      if q == 'op1' or q == 'op2':
        verificaroperacao = True
        opcaocontagem.append(a[1])
        opcaocontagem = [ x for x in opcaocontagem if x != 'op1' ]
        opcaocontagem = [ x for x in opcaocontagem if x != 'op2' ]
        bufferopcaocontagem = True
     
    
    buffer = 0
    if verificaroperacao == True:
      for j in a:
        if j == '*' or j == '+' or j == '-' or j == '+':
          buffer = j
      if buffer == '*':

        primtermo = float(opcaocontagem[0])
        segtermo = float(opcaocontagem[1])
        contaPronta = primtermo * segtermo
        print(
          '{} * {} ='.format(float(opcaocontagem[0]), float(opcaocontagem[1])),
          ' %.3f' % contaPronta)
        listapronta.append(contaPronta)

      if buffer == '+':
        primtermo = float(opcaocontagem[0])
        segtermo = float(opcaocontagem[1])
        contaPronta = primtermo + segtermo
        print(
          '{} + {} ='.format(float(opcaocontagem[0]), float(opcaocontagem[1])),
          ' %.3f' % contaPronta)
      if buffer == '-':
        primtermo = float(opcaocontagem[0])
        segtermo = float(opcaocontagem[1])
        contaPronta = primtermo - segtermo
        print(
          '{} - {} ='.format(float(opcaocontagem[0]), float(opcaocontagem[1])),
          ' %.3f' % contaPronta)
      if buffer == '/':

        primtermo = float(opcaocontagem[0])
        segtermo = float(opcaocontagem[1])
        contaPronta = primtermo / segtermo
        print(
          '{} / {} ='.format(float(opcaocontagem[0]), float(opcaocontagem[1])),
          ' %.3f' % contaPronta)
    
    print("linha {}".format(len(verificar)), "lexemas: ", f" {i} ")
        
    if removerInterrog == True:
      for interrog in a:
        if interrog == '*':
          a = [ x for x in a if x != '?' ]
          a = [ x for x in a if x != '*' ]
          firsttermo = int(a[0])
          second = int(listapronta[0])
          print('{} / {} ='.format(float(opcaocontagem[0]), float(opcaocontagem[1])), ' %.3f' % (firsttermo * second))
          
    if bufferopcaocontagem == True:
      a = [ x for x in a if x != 'op1' ]
      a = [ x for x in a if x != 'op2' ]
      a = [ x for x in a if x != '' ]
      buffer = a[0]
      if buffer == '*':
        primtermo = float(opcaocontagem[0])
        segtermo = float(opcaocontagem[1])
        contaPronta = primtermo * segtermo
        print(
          '{} * {} ='.format(float(opcaocontagem[0]), float(opcaocontagem[1])),
          ' %.3f' % contaPronta)
      if buffer == '+':
        primtermo = float(opcaocontagem[0])
        segtermo = float(opcaocontagem[1])
        contaPronta = primtermo + segtermo
        print(
          '{} + {} ='.format(float(opcaocontagem[0]), float(opcaocontagem[1])),
          ' %.3f' % contaPronta)
      if buffer == '-':
        primtermo = float(opcaocontagem[0])
        segtermo = float(opcaocontagem[1])
        contaPronta = primtermo - segtermo
        print(
          '{} - {} ='.format(float(opcaocontagem[0]), float(opcaocontagem[1])),
          ' %.3f' % contaPronta)
      if buffer == '/':
        primtermo = float(opcaocontagem[0])
        segtermo = float(opcaocontagem[1])
        contaPronta = (primtermo / segtermo)
        print(
          '{} / {} ='.format(float(opcaocontagem[0]), float(opcaocontagem[1])),
          ' %.3f' % contaPronta)

      if buffer == '+':
        primtermo = float(opcaocontagem[0])
        segtermo = float(opcaocontagem[1])
        contaPronta = primtermo + segtermo
        print(
          '{} + {} ='.format(float(opcaocontagem[0]), float(opcaocontagem[1])),
          ' %.3f' % contaPronta)
      if buffer == '-':
        primtermo = float(opcaocontagem[0])
        segtermo = float(opcaocontagem[1])
        contaPronta = primtermo - segtermo
        print(
          '{} - {} ='.format(float(opcaocontagem[0]), float(opcaocontagem[1])),
          ' %.3f' % contaPronta)
      if buffer == '/':

        primtermo = float(opcaocontagem[0])
        segtermo = float(opcaocontagem[1])
        contaPronta = (primtermo / segtermo)
        print(
          '{} / {} ='.format(float(opcaocontagem[0]), float(opcaocontagem[1])),
          ' %.3f' % contaPronta)
        
    if len(a) == 2 and a[0] == 'sin':
      angulo = int(a[1])
      seno = math.sin(math.radians(angulo))
      print("seno de {} é {}".format(angulo, seno))
      print("linha {}".format(len(verificar)), "sintaxe: valido ")


      
    elif len(a) == 2 and a[0] == 'cos':
      angulo = int(a[1])
      seno = math.cos(math.radians(angulo))
      print("cosseno de {} é {}".format(angulo, seno))
    elif len(a) == 3 and a[0] == 'exp':
      denominador = int(a[1])
      elevador = int(a[2])
      print(a[1], "elevado a", a[2], "é", denominador**elevador)
    elif len(a) == 3 and a[0] == 'rot':
      raiz = math.sqrt(int(a[1]))
      print("a raiz quadrada é", raiz)

    
    elif len(a) > 3 and verificaroperacao == False:
      listNovo = []
      for g in a:
        elemento = g
        a = list(string.ascii_lowercase)
        for p in a:
          elemento = elemento.replace(p, "")
        listNovo.append(elemento)
    
      for x in listNovo.copy():
          if x == '':
              listNovo.remove(x)
      validadorparenteses = False
      contagemdelistas = []
      for i in listNovo:
        contagemdelistas.append(i)
      if contagemdelistas[2] == '+':
        primtermo = float(contagemdelistas[0])
        segtermo = float(contagemdelistas[1])
        print(
          '{} + {} ='.format(float(contagemdelistas[0]), float(contagemdelistas[1])),
          ' %.3f' % (primtermo + segtermo))
    
      if contagemdelistas[2] == '-':
        primtermo = float(contagemdelistas[0])
        segtermo = float(contagemdelistas[1])
        print(
          '{} - {} ='.format(float(contagemdelistas[0]), float(contagemdelistas[1])),
          ' %.3f' % (primtermo - segtermo))
      if contagemdelistas[2] == '*':
        
        primtermo = float(contagemdelistas[0])
        segtermo = float(contagemdelistas[1])
        print(
          '{} * {} ='.format(float(contagemdelistas[0]), float(contagemdelistas[1])),
          ' %.3f' % (primtermo * segtermo))
      if contagemdelistas[2] == '/':
        
        primtermo = float(contagemdelistas[0])
        segtermo = float(contagemdelistas[1])
        print(
          '{} / {} ='.format(float(contagemdelistas[0]), float(contagemdelistas[1])),
          ' %.3f' % (primtermo / segtermo))
        
  
    if len(a) > 2 and verificaroperacao == False:
      
      contagemdelistas = []
      for i in a:
        contagemdelistas.append(i)
      if contagemdelistas[2] == '+':
        primtermo = float(contagemdelistas[0])
        segtermo = float(contagemdelistas[1])
        print(
          '{} + {} ='.format(float(contagemdelistas[0]), float(contagemdelistas[1])),
          ' %.3f' % (primtermo + segtermo))
    
      if contagemdelistas[2] == '-':
        primtermo = float(contagemdelistas[0])
        segtermo = float(contagemdelistas[1])
        print(
          '{} - {} ='.format(float(contagemdelistas[0]), float(contagemdelistas[1])),
          ' %.3f' % (primtermo - segtermo))
      if contagemdelistas[2] == '*':
        primtermo = float(contagemdelistas[0])
        segtermo = float(contagemdelistas[1])
        print(
          '{} * {} ='.format(float(contagemdelistas[0]), float(contagemdelistas[1])),
          ' %.3f' % (primtermo * segtermo))
      if contagemdelistas[2] == '/':
    
        primtermo = float(contagemdelistas[0])
        segtermo = float(contagemdelistas[1])
        print(
          '{} / {} ='.format(float(contagemdelistas[0]), float(contagemdelistas[1])),
          ' %.3f' % (primtermo / segtermo))
    if validadorparenteses == True:
      print("linha {}".format(len(verificar)), "sintaxe: invalido")
      validadorparenteses = False
    else:
      if validadornumerolistas == True:
        print("linha {}".format(len(verificar)), "sintaxe: valido")
    if validadornumerolistas == False:
      print("linha {}".format(len(verificar)), "sintaxe: invalido")
