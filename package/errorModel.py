#Importamos el modulo math para poder utilizar su funcion isnan()
import math

#Creamos el error que debe arrojarse cuando el usuario ingresa algo que no es un numero
class NaNError(Exception):
    def __init__ (self):
        self.message = "El parametro ingresado no es un numero"
        super().__init__(self.message)

#Creamos la funcion que chequea si el parametro ingresado es un numero. De no serlo, arroja el error creado.
def isNaN(value):
    try: 
        if math.isnan(value):
            raise NaNError()
    except ValueError:
        raise NaNError()

#Hacemos lo mismo para parametros vacios.
class EmptyError(Exception):
    def __init__ (self):
        self.message = "No se puede ingresar un parametro vacio"
        super().__init__(self.message)

def isEmpty(value):
    if value is None:
        raise EmptyError()
    if len(value.strip()) == 0:
        raise EmptyError()