class Animal:
    def __init__(self,nome,cor,comida):
        self.nome = nome
        self.cor = cor
        self.comida = comida
    def comer(self):
        print(f"o {self.nome} foi comer...")
class Gato(Animal):
    def init (self,nome,cor,comida):
        super(). __init__(nome,cor,comida)

    def miar(self):
        print(f"o {self.nome} foi miando...")
    def comer(self):
            print(f"o {self.nome} está comendo {self.comida}")

class Cachorro(Animal):
    def init(self,nome,cor,comida):
        super(). __init__(nome,cor,comida)

    def latir(self):
        print(f"o {self.nome} estava latindo pra pegar a canela do motoboy")
    def comer(self):
        print(f"o {self.nome} está comendo {self.comida}")

class Vaca(Animal):
    def init(self,nome,cor,comida):
        super(). __init__(nome,cor,comida)

    def mugir(self):
        print(f"A {self.nome} está mugindo para seu filhote")
    def comer(self):
        print(f"o {self.nome} está comendo {self.comida}")

class Coelho(Animal):
    def init(self,nome,cor,comida):
        super(). __init__(nome,cor,comida)

    def pular(self):
        print(f"o {self.nome} estava pulando")
    def comer(self):
        print(f"o {self.nome} está comendo {self.comida}")

class ingresso:
    def __init__(self, valor ):
        self.valor = valor

    def comprar(self):
        print(f"comprasse um ingresso no valor de {self.valor}")
class Vip(ingresso):
    def __init__ (self, valor):
        super().__init__(valor*1.5)

class Formas:
    def __init__(self, area, perimetro):
        self.base = area
        self.altura = perimetro
        self.soma = 0
        self.soma2= 0

class triangulo(Formas):
    def calculo(self):
        self.soma = (self.base * self.altura) /2
        print(self.soma2)


    def triangulo(self):
        print(f"o triangulo tem uma area de {self.soma2} ")
