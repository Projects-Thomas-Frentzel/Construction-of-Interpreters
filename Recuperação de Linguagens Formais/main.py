#Thomas Frentzel
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
  file = get_file(f"txt{counterwhile}.txt").split("\n")
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