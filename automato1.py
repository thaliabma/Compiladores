
def ehValido(entrada):
    fim = int(entrada[len(entrada)-1])
    estado_final = 1
    for i in range(len(entrada)):
      digito = int(entrada[i])
      if digito == 0:
        print('Estado q1 = 0')
        estado_final = 0
      else:
        print('Estado q2 = 1')
        estado_final = 1
    if(estado_final == 1):
      print('CADEIA RECONHECIDA')
    else:
      print('CADEIA NÃO RECONHECIDA')



entrada = input('Insira sua entrada: ')
ehValido(entrada)