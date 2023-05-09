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
    opcion = input("¿Quieres repetir el flujo secuencial?")
