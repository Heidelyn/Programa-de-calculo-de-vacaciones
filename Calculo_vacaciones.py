#Programa que calcula la cantidad de vacaciones que le corresponden a los empleados según su antigüedad y departamento


print('**Sistema de control vacacional Compañía AC**')

nombre = input('Por favor ingresa tu nombre: ')

d = int(input("Ingresa 1 para Operaciones, 2 para RRHH y 3 para Gerencia: "))

if d < 1 or d > 3:
    print('La clave de departamento ingresada es invalida')
    exit()

ant = float(input("Ingresa tu antiguedad en años: "))


def vacaciones(nom, tabla_ant):
    if ant < 1:
        print(nom, '----Le corresponden', tabla_ant[0],  'días de vacaciones')
    elif ant <= 2:
        print(nom, '----Le corresponden', tabla_ant[1],  'días de vacaciones')
    elif ant < 7:
        print(nom, '----Le corresponden', tabla_ant[2],  'días de vacaciones')
    elif ant >= 7:
        print(nom, '----Le corresponden', tabla_ant[3],  'días de vacaciones')


# Estas listas contienen los parámetros de días de vacaciones según departamento
d1_tabla = [0, 6, 14, 20]

d2_tabla = [0, 7, 15, 22]

d3_tabla = [0, 10, 20, 30]

if d == 1:
    vacaciones(nombre, d1_tabla)
elif d == 2:
    vacaciones(nombre, d2_tabla)
elif d == 3:
    vacaciones(nombre, d3_tabla)
