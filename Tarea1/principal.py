import Clases as C
from uuid import uuid4

if __name__ == "__main__":

    # Se instancian 2 financieras
    financiera_1 = C.Financiera("Saka Lukas", 100000000)
    financiera_2 = C.Financiera("Banco de Talca", 100000000)

    # Se instancian 8 clientes
    cliente_1 = C.Cliente("Wolverine", uuid4(), 500000)
    cliente_2 = C.Cliente("Ciclope", uuid4(), 400000)
    cliente_3 = C.Cliente("Snoopy", uuid4(), 300000)
    cliente_4 = C.Cliente("Perro Chocolo", uuid4(), 600000)
    cliente_5 = C.Cliente("Vaca Loca", uuid4(), 100000)
    cliente_6 = C.Cliente("Perro Firulais", uuid4(),200000)
    cliente_7 = C.Cliente("Chupacabras", uuid4(), 100000)
    cliente_8 = C.Cliente("Baby Yoda", uuid4(), 700000)

    # Se agrupan clientes en listas de 4 unidades
    cliente_grupo_A = [cliente_1, cliente_2, cliente_3, cliente_4]
    cliente_grupo_B = [cliente_5, cliente_6, cliente_7, cliente_8]

    # Se dan de alta los clientes del grupo_a en financiera_1
    for cliente in cliente_grupo_A:
        financiera_1.agregar_clientes(cliente)

    # Se dan de alta los clientes del grupo_b en financiera_2
    for cliente in cliente_grupo_B:
        financiera_2.agregar_clientes(cliente)

    # Se imprime resumen de clientes (id parcial, saldo y nombre)
    # de financiera_1
    print("\nSaldos de clientes antes de transferencia")
    for cliente in financiera_1.resumen_clientes():
        print(cliente)

    # Calcula máximo monto que financiera puede transferir
    maximo_monto_transferible_1 = financiera_1.maximo_transferible()
    print("\nEl máximo monto transferible es: ", maximo_monto_transferible_1)

    # Transfiere el máximo monto transferible de financiera_1
    financiera_1.transferir(financiera_1.id, cliente_2.id,
                            maximo_monto_transferible_1)

    print("\nSaldos de clientes antes de transferencia")
    for cliente in financiera_1.resumen_clientes():
        print(cliente)

    # Prueba de eliminación de cliente desde financiera
    # Pierde nombre financiera y linea_credito
    print("\n\nPROBANDO ELIMINACIÓN DE CLIENTE")
    print("\nAtributos del cliente_1 antes de ser eliminado")
    print("Aún están linea_credito y financiera")
    print("pues aún pertenece a financiera")
    print(cliente_1.atributos)

    # Elimina cliente_1 de financiera_1
    financiera_1.eliminar_cliente(cliente_1.id)

    print("\n\nAtributos del cliente_1 después de ser eliminado")
    print("ya no existen linea_credito y financiera pues ya no")
    print("pertenece a financiera")
    print(cliente_1.atributos)
