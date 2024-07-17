class Bicicleta:
    
    def __init__(self, cor , modelo, ano , valor) :

        # construtor   pode ser usado self ou this
        self.cor = cor
        self.modelo = modelo
        self.ano= ano
        self.valor = valor
 

    def buzinar(self):
        print ("Plim plim")

    def parar(self):
        print("Parando Bicicleta ...")
        print("Bicicleta parada!")

    def correr(self):
        print("vrumm")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


# b1 = Bicicleta("vermelha", "caloi", 2022,600)
# b1.buzinar()
# b1.correr()
# b1.parar()


b2 = Bicicleta('verde',"monark", 2000, 189)

print (b2 )