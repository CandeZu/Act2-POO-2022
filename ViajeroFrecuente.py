class Viajero:
    __numViajero = 0
    __dni = ""
    __nombre = ""
    __apellido = ""
    __millasAcum = 0

    def __init__(self, dni, nombre, apellido):
        self.__numViajero += 1
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millasAcum = 0
    
    def cantidadMillas(self):
        return self.__millasAcum
    
    def acumularMillas(self, millas):
        self.__millasAcum += millas

    def canjearMillas(self, millas):
        if self.__millasAcum >= millas:
            return self.__millasAcum
        else:
            print("No tiene suficientes millas acumuladas.")
    
