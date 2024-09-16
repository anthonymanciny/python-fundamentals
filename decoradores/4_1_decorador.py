def meu_decorador(funcao):
    def envelope():
        print('Faz algo antes de executar')
        funcao()
        print("Faz algo depois de executar")

    return envelope

def ola_mundo():
    print('Anthony')

ola_mundo = meu_decorador(ola_mundo)
ola_mundo()