from uuid import uuid4


class Cliente:

   # "self.__saldo" es Saldo Privado. En caso de error, cambiarlo a "self.saldo"
   def __init__(self, nombre, saldo):
        self.__id = uuid4()
        self.__nombre = nombre
        # self.__saldo es para "saldo privado" de cada cliente.
        self.__saldo = saldo
        self.__atributos = []

    def girar(self, monto):
        self.__saldo -= monto
        return self.__saldo

    def abonar(self, monto):
        self.__saldo += monto
        return self.__saldo

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @property
    def atributos(self):
        lista_atributos = list()
        for atributo in dir(self):
            if atributo[0] !="_":
                lista_atributos.append(atributo)
        return lista_atributos
