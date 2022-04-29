class Viajero:
    __numViajero = 0
    __dni = ""
    __nombre = ""
    __apellido = ""
    __millasAcum = 0

    def __init__(self, numViajero, dni, nombre, apellido, millasAcum):
        self.__numViajero = numViajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millasAcum = millasAcum
    
    def __str__(self):
        return "Numero de viajero: {}\nDNI: {}\nNombre: {}\nApellido: {}\nMillas acumuladas: {}".format(self.__numViajero, self.__dni, self.__nombre, self.__apellido, self.__millasAcum)
        
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
    
