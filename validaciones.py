# PROYECTO FINAL - INVENTARIO SQLITE, Curso introduccion a Python - Talento Tech
# Alumno : Rodrigo Bedoya 
# Comision : 26101
#======================================================================
#   MODULO DE VALIDACIONES                                           ||
#======================================================================
# VALIDACIONES GENERALES
def esNumero(string:str) -> bool:
    """
    PROPOSITO: Indica si un string dado es completamente numerico
    """
    return string.isdigit()

def estaEntreRangoInclusivo(inicio:int, final:int, x:int) -> bool:
    """
    PROPOSITO: Indica si la x dada se encuentra entre el rango [inicio ; final], incluye extremos
    """
    return inicio <= x <= final

def esVacio(string:str) -> bool:
    """
    PROPOSITO: Indica si un string es vacio o se compone de un solo espacio
    """
    return string == "" or string == " "

#=====================================================================================
# VALIDACION DE OPCIONES

def esOpcionValida(x:int, y:int, opcion_ingresada:str) -> bool:
    """
    PROPOSITO: Indica si la opcion ingresada por el usuario es valida
    NOTA: Se considera una opcion valida a un numero entre x e y, inclusivo.
    """
    if esNumero(opcion_ingresada): # no hago un AND entre las dos, por si acaso
        return estaEntreRangoInclusivo(x,y, int(opcion_ingresada))
    # Si no es un numero, es invalido
    return False


#======================================================================================
# VALIDACIONES SOBRE PRODUCTOS
def esNombreDeProductoValido(nombre:str) -> bool:
    """
    PROPOSITO: Indica si el nombre dado es un nombre valido para un producto
    NOTA: Se considera un nombre valido a un string que no es vacio ni numerico
    """
    return (not esNumero(nombre)) and (not esVacio(nombre))

def esCategoriaDeProductoValida(categoria:str) -> bool:
    """
    PROPOSITO: Indica si la categoria dada es una categoria valida para un producto
    NOTA: Se considera una categoria valida a un string que no es vacio ni numerico
    """
    return (not esNumero(categoria) and (not esVacio(categoria)))

def esStockDeProductoValido(stock:str) -> bool:
    """
    PROPOSITO: Indica si un stock dado es valido
    NOTA: Se considera un stock valido a un string no vacio, numerico mayor o igual a cero
    """
    if (not esVacio(stock) and esNumero(stock)):
        #Si es un numero, verifica que sea mayor o igual a cero
        return int(stock) >= 0
    # Si no es numerico, falla
    return False 

def esPrecioDeProductoValido(precio:str) -> bool:
    """
    PROPOSITO: Indica si el precio dado es valido
    NOTA: Se considera un precio valido a un string no vacio, numerico  y mayor o igual a cero
    """
    if (not esVacio(precio) and esNumero(precio)):
        #Si es un numero, verifica que sea mayor o igual a cero
        return int(precio) >= 0
    # Si no es numerico, falla
    return False 

def esIdValido(id:str) -> bool:
    """
    PROPOSITO: Indica si el ID de un producto es valido
    NOTA: Se considera un ID valido a un string numerico no vacio y mayor a cero
    """
    if (not esVacio(id) and esNumero(id)):
        #Si es un numero, verifica que sea mayor o igual a cero
        return int(id) >= 0
    # Si no es numerico, falla
    return False 