# PROYECTO FINAL - INVENTARIO SQLITE, Curso introduccion a Python - Talento Tech
# Alumno : Rodrigo Bedoya 
# Comision : 26101

import sqlite3 as sq
from validaciones import *
from colorama import Fore, Style 

LINEA = "="*60              # esto me va a ayudar a separar un poco los prints
OPCIONES_OFRECIDAS = 5      # Sin contar la opcion de salir (que seria el 0)
DATABASE = "inventario.db"  # nombre de la base de datos (siempre va a ser igual para la consigna)
programa_funcionando = True # una variable que permite cortar el programa si se desea

def iniciarBaseDeDatos():
    """
    PROPOSITO: Crea la tabla "productos" en la base de datos "inventario.db", si esta no existe.
    NOTA: Si la base de datos todavia no fue creada, la crea y tambien crea la tabla de productos.
    """
    conexion = sq.connect(DATABASE)
    cursor = conexion.cursor()

    creacion_de_tabla = """
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        categoria TEXT NOT NULL,
        stock INTEGER NOT NULL,
        precio REAL NOT NULL
    );
    """
    cursor.execute(creacion_de_tabla)
    conexion.close()

def MostrarMensajeDePresentacion():
    """
    PROPOSITO: Imprime en consola el mensaje de presentacion al usuario
    """
    print (Fore.GREEN + "\n¡¡ Bienvenido al sistema de gestion de productos !!")
    print (Style.RESET_ALL)

def MostrarOpciones():
    """
    PROPOSITO: Imprime en consola las opciones disponibles para el usuario
    """
    print(Fore.GREEN + LINEA) # El color de esta linea se va a heredar a lo demas
    print("\nPor favor, elija la accion que desea realizar:\n")
    # OPCIONES DISPONIBLES
    # 1 - Ingresar nuevo producto
    print("1 - Ingresar nuevo producto (requiere nombre, categoria, stock y precio)")
    # 2 - Ver productos ingresados
    print("2 - Ver todos los productos")
    # 3 - Buscar producto por su nombre
    print("3 - Buscar producto (Ingresar ID del producto, o su nombre semejante)")
    # 4 - Eliminar producto especifico
    print("4 - Eliminar producto especifico (ingresar ID del producto)") 
    # 5 - Actualizar producto especifico
    print("5 - Actualizar producto especifico (ingresar ID del producto)")
    # 0 - Salir
    print("0 - Salir")
    print(Style.RESET_ALL)

def IngresarOpcion():
    """
    PROPOSITO: Pide al usuario seleccionar una opción de las presentadas por el programa
    PRECONDICION: La opcion ingresada debe ser un numero entre 0 y la cantidad de instrucciones ofrecidas, inclusivo.
    """
    while True:
        opcion_elegida = input(Fore.GREEN + f"Por favor, seleccione la accion a realizar (0-{OPCIONES_OFRECIDAS}): ").strip() # normalizo entrada
        if esOpcionValida(0,OPCIONES_OFRECIDAS,opcion_elegida):
            print(Style.RESET_ALL)
            break
        else:
            print(Fore.RED + f"\nERROR: La accion elegida es invalida. Debe ser un numero entre 0 y {OPCIONES_OFRECIDAS}...\n")
            print(Style.RESET_ALL)
            # y vuelve a preguntar...

    return int(opcion_elegida)

def SeleccionarOpcion(opcion_elegida):
    """
    PROPOSITO: Dada una opcion ingresada por el usuario, selecciona y ejecuta la opcion elegida
    PRECONDICIONES: La opcion dada debe ser valida
    """

    if opcion_elegida == 1:
        # AGREGAR NUEVO PRODUCTO
        AgregarNuevoProducto()

    elif opcion_elegida == 2:
        # MOSTRAR TODOS LOS PRODUCTOS
        MostrarTodosLosProductos()

    elif opcion_elegida == 3:
        # BUSCAR PRODUCTO ESPECIFICO, por nombre semejante o por id
        BuscarProducto()

    elif opcion_elegida == 4:
        # ELIMINAR PRODUCTO ESPECIFICO, por id
        EliminarProducto()

    elif opcion_elegida == 5:
        # ACTUALIZAR PRODUCTO ESPECIFICO, por id
        ActualizarProducto()

    elif opcion_elegida == 0:
        # SALIR
        SalirDelPrograma()


#===============================================================================
#===============================================================================
# OPCION 1 , AGREGAR UN NUEVO PRODUCTO

def AgregarNuevoProducto():
    """
    PROPOSITO: Pide al usuario los datos del producto nuevo a ingresar
    """
    print(Fore.GREEN + LINEA)
    print("Creando nuevo producto: \n")

    nombre_producto = IngresarNombreProducto()
    categoria_producto = IngresarCategoriaProducto()
    stock_producto = IngresarStockProducto()
    precio_producto = IngresarPrecioProducto()

    datos_producto = (nombre_producto, categoria_producto, stock_producto, precio_producto)

    AgregarNuevoProductoABaseDeDatos(datos_producto)

def IngresarNombreProducto():
    """
    PROPOSITO: Pide al usuario ingresar el nombre para un producto, si es valido lo retorna, en caso contrario lo vuelve a pedir hasta que sea valido.
    """
    while True:
        nombre_producto = input(Fore.GREEN + "\nIngrese el nombre del producto: ").lower().strip()       # normalizo entrada
        if esNombreDeProductoValido(nombre_producto): #se encuentra en validaciones.py
            # Si es valido, lo retorno
            return nombre_producto
        # Sino...
        ImprimirError("El nombre ingresado no es valido. (No debe ser vacio ni un numero). Por favor, intente otra vez...")

def IngresarCategoriaProducto():
    """
    PROPOSITO: Pide al usuario ingresar la categoria para un producto, si es valida lo retorna, en caso contrario lo vuelve a pedir hasta que sea valida.
    """
    while True:
        categoria_producto = input(Fore.GREEN + "\nIngrese la categoria del producto: ").lower().strip() # normalizo entrada
        if esCategoriaDeProductoValida(categoria_producto):
            return categoria_producto 
        # Sino...
        ImprimirError("La categoria ingresada no es valida. (No debe ser vacia ni un numero). Por favor, intente otra vez...")

def IngresarStockProducto():
    """
    PROPOSITO: Pide al usuario ingresar el stock para un producto, si es valido lo retorna, en caso contrario lo vuelve a pedir hasta que sea valido.
    """
    while True:
        stock_producto = input(Fore.GREEN + "\nIngrese el stock del producto: ").strip() # normalizo entrada
        if esStockDeProductoValido(stock_producto):
            # Si es valido, lo retorno
            return int(stock_producto)
        # Sino...
        ImprimirError("El stock ingresado no es valido. (Debe ser un entero mayor o igual a cero). Por favor, intente otra vez...")

def IngresarPrecioProducto():
    """
    PROPOSITO: Pide al usuario ingresar el precio para un producto, si es valido lo retorna, en caso contrario lo vuelve a pedir hasta que sea valido.
    """
    while True:
        precio_producto = input(Fore.GREEN + "\nIngrese el precio del producto: ").strip()
        if esPrecioDeProductoValido(precio_producto):
            # Si es valido lo retorno
            return float(precio_producto)
        # Sino...
        ImprimirError("El precio del producto no es valido. (Debe ser un numero real mayor a cero). Por favor, intente otra vez...")


def ImprimirError(error:str) -> None:
    """
    PROPOSITO: Dada la descripcion de un error, lo imprime en consola con el color rojo
    """
    print(Fore.RED + f"ERROR: {error.strip()}")
    print(Style.RESET_ALL)

def AgregarNuevoProductoABaseDeDatos(datos_producto):
    """
    PROPOSITO: Dada una tupla de datos de un nuevo producto, lo agrega a la base de datos.
    PRECONDICIONES: Los datos deben ser validos
    """
    conexion = sq.connect(DATABASE)
    cursor = conexion.cursor()

    cursor.execute("INSERT INTO productos (nombre, categoria, stock, precio) VALUES (?,?,?,?);", datos_producto)

    conexion.commit() # guardar datos
    conexion.close()  # cerrar conexion


#===============================================================================
#===============================================================================
# OPCION 2, MOSTRAR TODOS LOS PRODUCTOS

def MostrarTodosLosProductos():
    """
    PROPOSITO: Muestra en consola todos los productos de la base de datos
    """
    conexion = sq.connect(DATABASE)
    cursor = conexion.cursor()

    consulta_todos_los_productos = "SELECT * FROM productos"
    cursor.execute(consulta_todos_los_productos)
    todos_los_productos = cursor.fetchall()

    print(Fore.GREEN + "Todos los productos: \n")

    if todos_los_productos: #Si hay al menos uno
        MostrarProductos(todos_los_productos)
    
    print(Style.RESET_ALL)

def MostrarProductos(productos):
    """
    PROPOSITO: Dada una lista de tuplas que representan productos, imprime los datos de cada uno en consola
    """
    for producto in productos:
        MostrarProducto(producto)

def MostrarProducto(producto):
    """
    PROPOSITO: Dada una tupla de producto, imprime sus datos en consola
    """
    print(Fore.GREEN + f"ID:\t\t{producto[0]}")
    print(f"Nombre:\t\t{producto[1]}")
    print(f"Categoria:\t{producto[2]}")
    print(f"Stock:\t\t{producto[3]}")
    print(f"Precio:\t\t{producto[4]}")
    print(LINEA)
    print(Style.RESET_ALL)

#===============================================================================
#===============================================================================
# OPCION 3, BUSCAR PRODUCTOS, por nombre semenjante o por ID especifico

def BuscarProducto():
    """
    PROPOSITO: Busca un producto en la base de datos por id o por nombre
    """
    print(Fore.GREEN + LINEA)
    print("Buscando producto especifico: \n")

    while True:
        print("¿Por que parametro quiere buscar?: ")
        print("1 - Por ID")
        print("2 - Por Nombre")
    
        opcion_elegida= input("Ingrese la opcion elegida (1-2): ").strip() # normalizo entrada
        if esOpcionValida(1,2,opcion_elegida):
            break
        # Sino...
        ImprimirError("La opcion no es valida. Intente nuevamente...")
    
    # Si es valida...
    opcion_elegida = int(opcion_elegida)
    if opcion_elegida == 1:
        BuscarProductoPorID()
    
    elif opcion_elegida == 2:
        BuscarProductoPorNombre()

def BuscarProductoPorID():
    """
    PROPOSITO: Pide al usuario un ID y busca el producto en la base de datos
    PRECONDICIONES: Debe existir un producto con el id dado en la base de datos
    """
    while True:
        id_buscado = input(Fore.GREEN + "Por favor, ingrese el ID buscado: ")

        if esIdValido(id_buscado):

            conexion = sq.connect(DATABASE)
            cursor = conexion.cursor()

            busqueda_de_producto = "SELECT * FROM productos WHERE id = ?;"
            id_buscado = int(id_buscado)
            cursor.execute(busqueda_de_producto, (id_buscado,))

            resultado = cursor.fetchone()
            conexion.close()

            if resultado:
                print("\nProducto encontrado: ")
                MostrarProducto(resultado)
                break
            else:
                ImprimirError("No existe un producto con el ID dado")
                break
        # Si el ID no fue valido, lo vuelve a preguntar
        ImprimirError("El ID ingresado no es valido. (Debe ser un entero mayor a cero). Por favor, intente otra vez...")

def BuscarProductoPorNombre():
    """
    PROPOSITO: Pide al usuario un nombre para buscarlo en la base de datos de productos, si encuentra semejanzas las imprime
    """
    while True:
        nombre_buscado = input(Fore.GREEN + "Por favor, ingrese el nombre buscado: ").strip().lower()

        if esNombreDeProductoValido(nombre_buscado):

            conexion = sq.connect(DATABASE)
            cursor = conexion.cursor()

            busqueda_de_producto = "SELECT * FROM productos WHERE nombre LIKE ?;" #busca exactos y semejantes

            cursor.execute(busqueda_de_producto, (f"%{nombre_buscado}%",))

            resultado = cursor.fetchall()
            conexion.close()

            if resultado:
                print("\nProductos encontrados: ")
                MostrarTodosLosProductos()
                break
            else:
                ImprimirError("No existe un producto con el nombre dado, o semenjantes...")
                break

        # Si no es un nombre valido, lo vuelve a preguntar
        ImprimirError("El nombre ingresado no es valido. (Debe ser un string no vacio y no numerico). Por favor, intente otra vez...")


#===============================================================================
#===============================================================================
# OPCION 4, ELIMINAR PRODUCTO ESPECIFICO , POR ID

def EliminarProducto():
    """
    PROPOSITO: Pide al usuario que ingrese un ID, y elimina el producto con el ID dado
    """
    print(Fore.GREEN + LINEA)
    print("Eliminando PRODUCTO: \n")
    while True:
        id_a_eliminar = input("Ingrese el ID del producto que desea eliminar: ").strip() # normalizo

        if esIdValido(id_a_eliminar):
            id_a_eliminar = int(id_a_eliminar)
            EliminarProductoDeID(id_a_eliminar)
            break
        # Si no es valido, vuelve a preguntar el ID
        ImprimirError("El ID ingresado no es valido. (Debe ser un entero mayor a cero). Por favor, intente otra vez...")

def EliminarProductoDeID(id:int):
    """
    PROPOSITO: Dado un id de producto valido, elimina de la base de datos el producto con dicho ID
    PRECONDICIONES: El producto con el id dado debe existir en la base de datos, sino falla.
                    El id dado debe ser valido.
    """
    conexion = sq.connect(DATABASE)
    cursor = conexion.cursor()

    #primero pregunto si existe, porque sino tiene que fallar
    consulta_producto = "SELECT * FROM productos WHERE id = ?"
    cursor.execute(consulta_producto, (id,))
    producto_existe = cursor.fetchone()

    if producto_existe:
        eliminar_producto = "DELETE FROM productos WHERE id = ?"

        cursor.execute(eliminar_producto, (id,))

        conexion.commit() # guardo los cambios
        print("\nProducto eliminado con exito\n")
        print(Style.RESET_ALL)
    else:
        ImprimirError("No existe el producto con el ID dado en la base de datos")

    conexion.close()


#===============================================================================
#===============================================================================
# OPCION 5, ACTUALIZAR PRODUCTO ESPECIFICO, por id

def ActualizarProducto():
    """
    PROPOSITO: Pide al usuario ingresar un ID, y si es valido y el producto existe, entonces lo actualiza
    """

    while True:
        print(Fore.GREEN + LINEA)
        id_buscado = input("Ingrese el ID del producto que desea actualizar: ").strip() # normalizo
        # Si es ID valido
        if esIdValido(id_buscado):
            id_buscado = int(id_buscado)
            conexion = sq.connect(DATABASE)
            cursor = conexion.cursor()
            #fijarse si está
            consulta = "SELECT * FROM productos WHERE id = ?"

            cursor.execute(consulta, (id_buscado,))

            producto_existe = cursor.fetchone()

            # Si esta...
            if producto_existe:
                nombre_actual = producto_existe[1]
                categoria_actual = producto_existe[2]
                stock_actual = producto_existe[3]
                precio_actual = producto_existe[4]

                datos_viejos = (nombre_actual, categoria_actual, stock_actual, precio_actual)

                datos_nuevos = PedirNuevosDatos(datos_viejos)

                # si cambio algo, lo actualizo
                if datos_nuevos != datos_viejos:
                    #agrego el id al final para poder actualizarlo
                    datos_nuevos = datos_nuevos + (id_buscado,)

                    actualizar_producto_de_id = """
                    UPDATE productos
                    SET nombre = ?,
                        categoria = ?,
                        stock = ?,
                        precio = ?
                    WHERE id = ?
                    """

                    cursor.execute(actualizar_producto_de_id, datos_nuevos)
                    conexion.commit()

                    print("\nDatos actualizados correctamente\n")
                    print(Style.RESET_ALL)
                    conexion.close()
                    break
                #Sino, no hago nada...
                else:
                    print(Fore.GREEN + "\nNo hubo cambios\n")
                    print(Style.RESET_ALL)
                    conexion.close()
                    break

            else:
                # Si no existe, retorno error
                ImprimirError("El ID buscado no existe en la base de datos.")
                break



        # Si no es ID valido...
        ImprimirError("El ID ingresado no es valido. (Debe ser un entero mayor a cero). Por favor, intente otra vez...")

def PedirNuevosDatos(datos):
    """
    PROPOSITO: Dados datos viejos de un producto, pregunta al usuario cuales desea actualizar y retorna los datos actualizados.
    NOTA: Si algun dato no fue cambiado, se mantiene con el dato que tuvo antes.
    """
    # primero muestro los datos antiguos
    print("\nDatos antiguos:\n")
    print(f"Nombre anterior:\t{datos[0]}")
    print(f"Categoria anterior:\t{datos[1]}")
    print(f"Stock anterior:\t\t{datos[2]}")
    print(f"Precio anterior:\t{datos[3]}\n")

    # Pido los nuevos
    nuevo_nombre = input("Ingrese nuevo nombre (o presione Enter para quedarse con el antiguo dato): ").strip()
    #========
    # NOMBRE
    if nuevo_nombre == "":
        nuevo_nombre = datos[0]
    else:
        if esNombreDeProductoValido(nuevo_nombre):
            pass
        else:
            ImprimirError("El nombre ingresado no es valido. (Debe ser un string no vacio y no numerico). Por favor, intente otra vez...")
            nuevo_nombre = IngresarNombreProducto()

    nueva_categoria = input("Ingrese nueva categoria (o presione Enter para quedarse con el antiguo dato): ").strip()

    #=======
    # CATEGORIA
    if nueva_categoria == "":
        nueva_categoria = datos[1]
    else:
        if esCategoriaDeProductoValida(nueva_categoria):
            pass
        else:
            ImprimirError("La categoria ingresada no es valida. (Debe ser un string no vacio y no numerico). Por favor, intente otra vez...")
            nueva_categoria = IngresarCategoriaProducto()

    #=======
    # STOCK
    nuevo_stock = input("Ingrese nuevo stock (o presione Enter para quedarse con el antiguo dato): ").strip()

    if nuevo_stock == "":
        nuevo_stock = datos[2]
    else:
        if esStockDeProductoValido(nuevo_stock):
            pass
        else:
            ImprimirError("El stock ingresado no es valido. (Debe ser un string no vacio, numerico y mayor o igual a cero). Por favor, intente otra vez...")
            nuevo_stock = IngresarStockProducto()

    #======
    # PRECIO
    nuevo_precio = input("Ingrese nuevo precio (o presione Enter para quedarse con el antiguo dato): ").strip()

    if nuevo_precio == "":
        nuevo_precio = datos[3]
    else:
        if esPrecioDeProductoValido(nuevo_precio):
            pass
        else:
            ImprimirError("El precio ingresado no es valido. (Debe ser un string no vacio, numerico y mayor a cero). Por favor, intente otra vez...")
            nuevo_stock = IngresarStockProducto()
    
    return (nuevo_nombre, nueva_categoria, nuevo_stock, nuevo_precio)
    







# OPCION 0, SALIR DEL PROGRAMA

def SalirDelPrograma():
    """
    PROPOSITO: Cambia el valor de la variable global "programa_funcionando" a False, para terminar el programa.
    """
    global programa_funcionando

    #mensaje de despedida
    print(Fore.GREEN + "\n¡¡ Gracias por utilizar nuestro sistema, hasta luego... !!")
    print(Style.RESET_ALL)

    #termina el programa
    programa_funcionando = False # al ponerlo en false, se rompe el bucle while del programa

if __name__ == "__main__":
    iniciarBaseDeDatos()
    MostrarMensajeDePresentacion()

    while (programa_funcionando):
        MostrarOpciones()
        opcion_elegida = IngresarOpcion()
        SeleccionarOpcion(opcion_elegida)
        

    
