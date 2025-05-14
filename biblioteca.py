class Animal():
    def init (self,nome,cor):
        super(). __init__(nome,cor)

    def miar(self):
        print(f"o {self.nome} foi miando")