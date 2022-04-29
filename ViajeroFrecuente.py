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
        print("Millas acumuladas:{}".format(self.__millasAcum))
        print("Millas a canjear: {}".format(millas))
        if(self.__millas_acum<millas):
            print("Millas insuficientes")
        else:
            self.__millasAcum = self.__millasAcum - millas
            print("".center(20,"-"))
            print("Millas canjeadas.\n")
            print("Millas totales: {}".format(self.__millasAcum))
            print("".center(20,"-"))
    
