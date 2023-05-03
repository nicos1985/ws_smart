def sel_click(png,x1=0,x2=0,w=gui.size()[0],h=gui.size()[1],x0=0, y0=0, grayscale=True):
    """Selecciona segun cordenadas de locate, mueve el mouse y hace clik en el punto indicado. Se pasan coordenadas y una png"""
    pass

def reg_log(archivo, mensaje, *args):
    """Registra un evento en el archivo indicado, hace un time stamp y los datos que se pasen por args."""
    pass

def encontrar_verde(pantalla,estado):
    """ Encuentra punto verde de aprobado en pantalla de monto"""
    pass

def guarda_info(archivo, dni_current, nombre_cli, estado, sexo, fecha_nac, monto_proc):
    """Guarda la info de la linea con todos los datos en el archivo."""
    pass

def cli_activo(pantalla,estado):
    """Hace clik en el cliente activo y mueve con scroll hacia abajo."""
    pass

def get_process(process_name):
    """Obtiene el proceso de google chrome de la lista de procesos de windows"""
    pass

def abrir_explorador():
    """ Abre el explorador Chrome y chequea que se haya abierto para continuar con el siguiente paso."""
    pass

def abre_incognito():
    """ Abre la ventana de incognito de chrome"""
    pass

def ingresa_smart(url):
    """ingresa a smart usando la url pasada."""
    pass

def log_in(mail, contrasena):
    """Ingresa mail y contraseña para ingresar a smart"""
    pass

def habilita_cursor():
    """habilita el modo de cursor para navegar y establece la pantalla al 100%"""
    pass

def busca_personas(pantalla, por_x, por_y, por_w, por_h, x0):
    """Busca el boton para realizar la busqueda de personas"""
    pass

def busco_dni(i):
    """Busca el dni siguiente en archivo de origen y lo coloca en el campo de busqueda. Da enter"""
    pass

def copia_datos_dni(pantalla, dni_current):
    """Copia los datos del dni encontrado y los deja en la variable cliente_proc, en caso de error, retorna el mismo."""
    pass

def ejecutar():
    """ejecuta el flujo del proceso. Construyendo"""
    pass

"""CHATGPT"""

def funcion1(parametros):
    # Código de la función 1
    contador = 0
    while contador < 2:
        if condicion1:
            return True
        else:
            contador += 1
    return False

def funcion2(parametros):
    # Código de la función 2
    contador = 0
    while contador < 2:
        if condicion2:
            return True
        else:
            contador += 1
    return False

def funcion3(parametros):
    # Código de la función 3
    contador = 0
    while contador < 2:
        if condicion3:
            return True
        else:
            contador += 1
    return False

# Parámetros para cada función en cada repetición
parametros1 = [[1,2],[3,4]]
parametros2 = [["a","b"],["c","d"]]
parametros3 = [True,False]

# Inicio del flujo secuencial
opcion = "si"

while opcion == "si":
    # Paso 1
    resultado = funcion1(parametros1.pop(0))
    if resultado:
        # Paso 2
        exito = True  # Variable de control
        for i in range(len(parametros2)):
            resultado = funcion2(parametros2[i])
            if resultado:
                # Paso 3
                exito = True  # Variable de control
                for j in range(len(parametros3)):
                    resultado = funcion3(parametros3[j])
                    if resultado:
                        print("Flujo secuencial exitoso")
                        exito = True  # Variable de control
                        break  # Sale del bucle de la función 3
                    else:
                        print("La función 3 ha fallado dos veces seguidas")
                        parametros2.insert(0, parametros2.pop(i+1))  # Mueve los parámetros a la posición inicial
                        parametros1.insert(0, parametros1.pop(1))
                        exito = False  # Variable de control
                        break  # Sale del bucle de la función 3
                if not exito:
                    break  # Sale del bucle de la función 2
            else:
                print("La función 2 ha fallado dos veces seguidas")
                parametros1.insert(0, parametros1.pop(1))
                parametros2.insert(0, parametros2.pop(i+1))  # Mueve los parámetros a la posición inicial
                exito = False  # Variable de control
                break  # Sale del bucle de la función 2
            if exito:
                break  # Sale del bucle de la función 2
        if not exito:
            parametros1.insert(0, parametros1.pop(1))
            continue  # Vuelve al paso 1
    else:
        print("La función 1 ha fallado dos veces seguidas")
        break  # Termina el flujo secuencial

    # Preguntar si se quiere repetir el flujo secuencial
    opcion = input("¿Quieres repetir el flujo secuencial?
