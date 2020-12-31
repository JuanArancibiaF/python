from uuid import uuid4


class Financiera:

    def __init__(self, nombre, saldo_institucional):
        self.__id = uuid4()
        self.__nombre = nombre
        self.__saldo_institucional = saldo_institucional
        self.__clientes = list()  # Al iniciar, las financieras no tienen clientes (en blanco)
        self.__sumatoria_lineas_credito = 0

    def agregar_cliente(self, cliente):
        # Si estamos dentro del 10% del saldo institucional, podemos agregar cliente.
        # como el cliente no existe para la financiera, asignamos al crear, la linea de credito.
        if self.__sumatoria_lineas_credito <= 0.1*self.__saldo_institucional:
            cliente.financiera = self.__nombre
            cliente.linea_credito = 1000000  # Asignamos a la línea de credito cliente un millón.
            self.__sumatoria_lineas_credito += 1000000
            # lo guardamos en la lista clientes de la financiera.
            self.__clientes.append(cliente)
            return self.__clientes

        else:
            raise Exception("Error:No hay capacidad para lineas de crédito!")

    def eliminar_cliente(self, id_cliente):
        for index, cliente in enumerate(self.__clientes):
            if cliente.id == id_cliente:
                delattr(cliente, "financiera")
                delattr(cliente, "linea_credito")
                self.__clientes.pop(index)
                return self.__clientes

    def transferir(self, id_origen, id_destino, monto):
        # revisamos si financiera es origen o destino
        if id_origen == self.__id:
            origen = self
        elif id_destino == self.__id:
            destino = self

        # como financiera no es origen ni destino entonce
        # se revisa si ambos son clientes
        cliente_origen_encontrado = False  # inicializo en "false" para evaluarlas.
        cliente_destino_encontrado = False
        for cliente in self.__clientes:
            if cliente.id == id_origen:
                origen = cliente
                cliente_origen_encontrado = True
            elif cliente.id == id_destino:
                destino = cliente
                cliente_destino_encontrado = True
        if (cliente_destino_encontrado == True
            and cliente_origen_encontrado == False
                and origen != self):
            raise Exception("El origen no se encontró!")
        elif (cliente_destino_encontrado == False
              and cliente_origen_encontrado == True
              and destino != self):
            raise Exception("El destino no se encontró!")
        if (cliente_destino_encontrado == False
                and cliente_origen_encontrado == False):
            raise Exception("El origen y el destino no fueron econtrados!")
        else:
            if isinstance(origen, Cliente):
                if (origen.saldo + origen.linea_credito) >= monto:
                    if isinstance(destino, Cliente):
                        destino.saldo += monto
                    elif isinstance(destino, Financiera):
                        destino.__saldo_institucional += monto
                    origen.saldo -= monto
                else:
                    raise Exception("Cliente origen con saldo insuficiente!")
            else:
                if ((origen.__saldo_institucional-monto)*.1
                    >= self.__sumatoria_lineas_credito):
                    destino.saldo += monto
                    origen.__saldo_institucional -= monto
                else:
                    message = "Financiera de origen con saldo insuficiente!"
                    raise Exception(message)

    def giros_totales(self):
        pass

    def resumen_clientes(self):
        '''
        Imprime lista de clientes de financiera
        con nombre, id parcial y saldo
        '''
        lista_datos_clientes = list()
        for cliente in self.clientes:
            lista_datos_clientes.append([str(cliente.id)[:5],
                                cliente.saldo,
                                         cliente.nombre])
        return lista_datos_clientes

    def maximo_transferible(self):
        maximo_monto_transferible = (self.__saldo_institucional
                                     - self.__sumatoria_lineas_credito/0.1)
        return maximo_monto_transferible


    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @property
    def saldo_institucional(self):
        return self.__saldo_institucional

    @property
    def clientes(self):
        return self.__clientes

    @property
    def sumatoria_lineas_credito(self):
        return self.__sumatoria_lineas_credito
