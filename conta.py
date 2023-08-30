class Conta:

    def __init__(self, agencia, numero, titular, saldo, limite=1000.0):
        
        self.__agencia = agencia
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def agencia(self):
        return self.__agencia
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return '001'

    def sacar(self, valor):
        if valor <= self.__limite + self.__saldo:
            self.__saldo -= valor
            return valor
        else:
            print("Seu saldo é insuficiente!")
            return 0

    def depositar(self, valor):
        self.__saldo += valor

    def extrato(self):
        print(f"Saldo {self.__saldo} da conta e limite {self.__limite}. Titular: {self.__titular}")