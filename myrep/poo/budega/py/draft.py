class Cliente:
    def __init__(self, nome:str):
        self.__nome = nome

    def getnome(self) -> str:
        return self.__nome 
    
    def toString(self):
        return f" Cliente(nome = '{self.__nome}')"
    
class Mercantil:
    def __init__(self, quantidadecaixa: int):
        self.qntcaixa = quantidadecaixa
        self.caixa = [None] * quantidadecaixa
        self.lista = []