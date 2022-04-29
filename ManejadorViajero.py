from ManejadorViajero import Viajero
import csv

class ManejadorViajero:
    __listaViajeros = []

    def __init__(self, listaViajeros):
        self.__listaViajeros = []
    

    def GenerarLista(self):
        archivo = open("Viajeros.csv")
        reader = csv.reader(archivo, delimiter=";")
        bandera=True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                numViajero = int(fila[0])
                dni = fila[1]
                nombre = fila[2]
                apellido = fila[3]
                millasAcum = int(fila[4])
                viajero = Viajero(numViajero, dni, nombre, apellido, millasAcum)
                self.__listaViajeros.append(viajero)
        archivo.close()


