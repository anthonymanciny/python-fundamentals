def verificador_ano_bissexto():
    ano = int(input())

# TODO: Verifique se o ano é bissexto utilizando uma estrutura de controle condicional, como if/else:


verificador_ano_bissexto()
if  ano % 4 == 0: 
      if ano % 100 == 0:
        if ano % 400 == 0:
          print ("SIM")
        else:
          print ("NÃO")
      else:
        print ("SIM")
else:
      print( "NÃO")