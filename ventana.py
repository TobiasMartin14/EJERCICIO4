

class Ventana():
    __titulo = ''
    __XsupIzq = ''
    __YsupIzq = ''
    __XinfDer = ''
    __YinfDer = ''

    def __init__ (self, titulo='', XsupIzq=0, YsupIzq=0, XinfDer=500, YinfIzq=500):
        self.__titulo = titulo
        self.__XsupIzq = max(0, XsupIzq)
        self.__YsupIzq = max(0, YsupIzq)
        self.__XinfDer = min(500, XinfDer)
        self.__YinfDer = min(500, YinfIzq)

    def mostrar (self):
        print ("Ventana {} con vertice superior izquierdo ({} , {}) y vertice inferior derecho ({} , {})" .format(self.__titulo, self.__XsupIzq, self.__YsupIzq, self.__XinfDer, self.__YinfDer))
    
    def getTitulo (self):
        return (self.__titulo)
    
    def alto (self):
        return (self.__XinfDer - self.__XsupIzq)
    
    def ancho (self):
        return (self.__XinfDer - self.__XsupIzq)
    
    def moverDerecha (self, xUn = 1):
        self.__XsupIzq = min(self.__XsupIzq + xUn, 500)
        self.__XinfDer = min(self.__XinfDer + xUn, 500)
    
    def moverIzquierda (self, xUn = 1):
        self.__XsupIzq = max(self.__XsupIzq - xUn, 0)
        self.__XinfDer = max(self.__XinfDer - xUn, 0)

    def bajar (self, xUn = 1):
        self.__YsupIzq = min(self.__YsupIzq + xUn, 500)
        self.__YinfDer = min(self.__YinfDer + xUn, 500)
    
    def subir (self, xUn = 1):
        self.__YsupIzq = max(self.__YsupIzq - xUn, 0)
        self.__YinfDer = max(self.__YinfDer - xUn, 0)
        
    
