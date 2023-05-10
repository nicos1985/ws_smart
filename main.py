import pyautogui as gui
import clipboard as clip
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfilename, askdirectory
import time
import PIL
from datetime import date, datetime
import os
from psutil import Process 
import psutil
import ast 


def sel_click(png,x1=0,x2=0,w=gui.size()[0],h=gui.size()[1],x0=0, y0=0, grayscale=True):
    """Selecciona segun cordenadas de locate, mueve el mouse y hace clik en el punto indicado. Se pasan coordenadas y una png"""
    #print(png)
    #print(f'x1:{x1}')
    #print(f'x2:{x2}')
    #print(f'w:{w}')
    #print(f'h:{h}')
    #gui.moveTo(x=(int(x1)), y=(int(x2)))
    #time.sleep(2)
    #gui.moveTo(x=(int(x1+w)), y=(int(x2+h)))
    #time.sleep(2)
    png_coordenadas = gui.locateCenterOnScreen(png, grayscale=grayscale, confidence=0.5, region=(x1,x2,w,h))
    #print(f'png_coordenadas{png_coordenadas}')
    gui.moveTo(x=(int(png_coordenadas[0])+x0), y=(int(png_coordenadas[1])+y0))
    gui.click(x=(int(png_coordenadas[0])+x0), y=(int(png_coordenadas[1])+y0), clicks=1, button='left')

    # si esta activo el cliente entonces sigue a la proxima pantalla para poder obtener el monto
def reg_log(archivo, mensaje, *args):
    """Registra un evento en el archivo indicado, hace un time stamp y los datos que se pasen por args."""
    now = datetime.now()
    time_stamp = now.strftime("%Y-%m-%d %H:%M:%S")
    with open(archivo, 'a') as archivo:
        archivo.write(f'{mensaje},{args},{time_stamp}\n') 

def a_reintentar_dni(dni_current, archivo, intentos=3):
    """agrega el dni a la lista de origen para poder reintentarlo"""
    with open(archivo, 'r') as arch_origen:
        contenido = arch_origen.read()
    
    dni = dni_current
    contador = contenido.count(dni)
    print(f'contador = {contador}')
    if contador <= intentos:
        with open(archivo, 'a') as archivo:
            archivo.write(f'{dni_current}\n')
        lista_dni.append(dni)
        print('actualiza lista')
        return 'agregado'
    else:
        error = f'el {dni_current} superó la cantidad de intentos'
        return error

def encontrar_verde(pantalla,estado):
    """ Encuentra punto verde de aprobado en pantalla de monto"""
    try:
          
        punto_verde = gui.locateCenterOnScreen('img/punto_verde.png', grayscale=True, confidence=0.8)
        gui.click(punto_verde, button="left")
        
        #print(punto_verde)

        click = gui.moveTo(int(punto_verde[0])+pantalla[0]*0.12,int(punto_verde[1])-pantalla[1]*0.15)

        gui.drag(98, 0,0.3)
        gui.hotkey('ctrl', 'c')
        monto = clip.paste()
        monto_proc = monto.replace("$", "").replace(" ", "").replace(".","")
        return monto_proc
    except:
        
        error = f'No se encuentra el punto verde'
        return error
    

def guarda_info(archivo_destino, dni_current, nombre_cli, estado, sexo, fecha_nac, monto_proc, unique):
    """Guarda la info de la linea con todos los datos en el archivo."""
    try:   
        now = datetime.now()
        #print(f'now :{now}')
        time_stamp = now.strftime("%Y-%m-%d %H:%M:%S")
        #print(f'time_stamp: {time_stamp}')
        print(f'Guardar Info: {dni_current},{nombre_cli},{estado},{sexo},{fecha_nac},{monto_proc},{time_stamp}')
        registro = (f'{dni_current},{nombre_cli},{estado},{sexo},{fecha_nac},{monto_proc},{time_stamp}')
        reg_proc = registro.splitlines()
        registro_fin = ''.join(reg_proc)
    
        print('antes de abrir el archivo')
        with open(f'{archivo_destino}/export-{unique}.txt', 'a') as arch:
            arch.write(f'{registro_fin},\n')
        fase = 'cargado'
        return fase
    except:
        error = 'no se pudo cargar el registro en el archivo'
        return error
        

def cli_activo(pantalla,estado):
    """Hace clik en el cliente activo y mueve con scroll hacia abajo."""
    if estado == "ACTIVO":
        print('es cliente activo')
        gui.click(pantalla[0]*0.5, pantalla[1]*0.75)
        sel_click('img/activo.png', int(pantalla[0]*0.12),int(pantalla[1]*0.20), int(pantalla[0]*0.50), int(pantalla[1]*0.50))
        gui.moveTo(pantalla[0]*0.4,pantalla[1]*0.5)
        time.sleep(2*tiempo_var.get())
        gui.scroll(-300)
        
        time.sleep(5*tiempo_var.get())
        x=1 
        return 'realizado'
    else:
        return 'no realizado'
        
       
def get_process(process_name):
    """Obtiene el proceso de google chrome de la lista de procesos de windows"""
    for process in psutil.process_iter(['pid','name']):
        if process.info['name'] == process_name:
            return process

def abrir_explorador():
    """ Abre el explorador Chrome y chequea que se haya abierto para continuar con el siguiente paso."""
    # abre chrome
    with gui.hold(['ctrl', 'alt']):
        gui.press('c')
    time.sleep(8*tiempo_var.get())
    """
    # maximiza
    gui.keyDown('alt')
    gui.keyDown('space')
    gui.press('x')
    gui.keyUp('alt')
    gui.keyUp('space')
    time.sleep(4*tiempo_var.get())
    """
    print("Busca chrome")
    ruta_chrome = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
    if os.path.exists(ruta_chrome):
        print("Chrome existe")

        nombre_proceso = "chrome.exe"
        # Obtener lista de procesos en ejecución
        p = get_process(nombre_proceso)
        print(f'proceso:{p}')
        if p is not None:
            print("Chrome está en ejecucion.")
            return "chrome ejecuto"
        else:
            print("Chrome no está en ejecucion.")
            return "chrome no ejecuto"
    else:
        print("El chrome no existe.")
        return "chrome no existe"

def abre_incognito():
    """ Abre la ventana de incognito de chrome"""
    #abre ventana incognito
    gui.hotkey('ctrl', 'shift', 'n')
    time.sleep(3*tiempo_var.get())
    
def ingresa_smart(url):
    """ingresa a smart usando la url pasada."""
    #ingresa a smart
    gui.hotkey('ctrl', 'l')
    smart_url = url
    clip.copy(smart_url)
    time.sleep(2*tiempo_var.get())
    gui.hotkey('ctrl', 'v')
    gui.press('enter')


def log_in(mail, contrasena):
    """Ingresa mail y contraseña para ingresar a smart"""
    #coloca mail y contraseña
    mail_smart = mail
    contra_smart = contrasena
    time.sleep(4*tiempo_var.get())
    gui.press('home')
    gui.press('del',50)
    clip.copy(mail_smart)
    gui.hotkey('ctrl', 'v')
    time.sleep(0.2)
    gui.press('enter')
    time.sleep(4*tiempo_var.get())
    clip.copy(contra_smart)
    gui.hotkey('ctrl', 'v')
    time.sleep(0.2)
    gui.press('enter')
    time.sleep(4*tiempo_var.get())
    #continua la sesion abierta
    try:
        gui.press('enter')
        time.sleep(1*tiempo_var.get())
        
        gui.press('enter')
        mensaje = "Se realizó la apertura del explorador. Se logueó correctamente"
        reg_log(f'{archivo_destino}\log{date.today()}.txt',mensaje)
        time.sleep(5*tiempo_var.get())

        return True
    except:
        mensaje = "No se pudo abrir el explorador o no se pudo realizar el logueo. Se reintenta"
        
        #Cerrar Chrome
        gui.keyDown('alt')
        gui.press('f4')
        gui.press('f4')
        gui.keyUp('alt')
        time.sleep(1*tiempo_var.get())
        return mensaje
        

def habilita_cursor():
    """habilita el modo de cursor para navegar y establece la pantalla al 100%"""
    #cambia a modo cursor para navegar
    gui.press('F7')
    time.sleep(0.5)
    gui.press('enter')
    time.sleep(0.5)
    #pantalla al 100%
    gui.hotkey('ctrl', '0')
    
def busca_personas(pantalla, por_x, por_y, por_w, por_h, x0):
    """Busca el boton para realizar la busqueda de personas"""
    
    try:
        sel_click('img/busqueda_personas.png',int(pantalla[0]*por_x),int(pantalla[1]*por_y), int(pantalla[0]*por_w), int(pantalla[1]*por_h),x0=x0)
        time.sleep(0.5)
        gui.press('tab',2)
        return 'buscar exitoso'
    
    except:
        
        error = f'No se encuentra busqueda personas'
        return error
    
def busco_dni(dni):
    """Busca el dni siguiente en archivo de origen y lo coloca en el campo de busqueda. Da enter"""

    #Traigo DNI del txt
    dni_current = dni
    #copio el DNI a portapapeles
    clip.copy(dni_current)
    #Pego el DNI en portapapeles
    gui.hotkey('ctrl', 'v')
    time.sleep(0.3)
    gui.press('enter')
    time.sleep(1*tiempo_var.get())
    return dni_current

def copia_datos_dni(pantalla, dni_current):
    """Copia los datos del dni encontrado y los deja en la variable cliente_proc, en caso de error, retorna el mismo."""
    try:
        select = gui.locateCenterOnScreen('img/marco2.png', grayscale=True, confidence=0.7)
        
        gui.moveTo(x=int(select[0]), y=int(select[1]*1.25))
        time.sleep(0.3)
        gui.drag(pantalla[0]*0.90,duration=0.3)
        time.sleep(0.3)
        print('por realizar ctrl C')
        gui.hotkey('ctrl', 'c')
        print('por pegar en cliente')
        cliente = clip.paste()
        
        print('por separar lineas')
        nombre_cli, estado, sexo, fecha_nac  = cliente.splitlines()
        print('hago un strip de la fecha nacimiento')
        fecha_nac_corr = fecha_nac.strip()
        print('transformo cliente en una lista con los datos ')
        cliente_proc = [nombre_cli, estado, sexo, fecha_nac_corr, dni_current]
        print(f'nombre: {nombre_cli},estado: {estado} , sexo: {sexo}, fecha nac: {fecha_nac_corr}, dni: {dni_current}')
        return cliente_proc
    except:
        error = 'error al copiar datos del cliente'
        return error


ventana = tk.Tk()
ventana.geometry('1000x750')
ventana.configure(bg='#93BDA5')
ventana.resizable(width=False, height=False)


#variables
link_var = tk.StringVar()
mail_var = tk.StringVar()
contrasena_var = tk.StringVar()
ruta_origen_var = tk.StringVar()
ruta_export_var = tk.StringVar()
tiempo_var = tk.DoubleVar()

#Funciones Vista
def elegir_origen():
    """Elige el origen de la ruta de los datos en txt"""
    ruta_origen_ent.configure(state='normal')
    ruta_origen_ent.delete(0, 'end')
    ruta_origen_var = askopenfilename()
    ruta_origen_ent.insert(0, ruta_origen_var)
    ruta_origen_ent.configure(state='readonly')
    return ruta_origen_var

def elegir_destino():
    """elige la ruta de destino donde guardara el txt"""
    ruta_destino_ent.config(state='normal')
    ruta_destino_ent.delete(0,'end')
    ruta_export_var = askdirectory()
    ruta_destino_ent.insert(0, ruta_export_var)
    ruta_destino_ent.config(state='readonly')
    return ruta_export_var

def guardar():
    """Guarda los parametros ingresados para recuperarlos en la proxima apertura"""
    parametros_dict = {'link': link_var.get(), 
                       'mail':mail_var.get(),
                       'contrasena': contrasena_var.get(), 
                       'ruta origen': ruta_origen_var.get(), 
                       'ruta export': ruta_export_var.get(),
                       'tiempo': tiempo_var.get()
                       }

    with open('parametros.txt', 'w') as param:
        
        param.write(f'{parametros_dict}')

link_ent = tk.Entry(ventana, textvariable = link_var, width=60, font=('Calibri', 11))
link_ent.grid(row=2, column=1, sticky='W', padx=5, pady=5)

link_ent = tk.Entry(ventana, textvariable = link_var, width=60, font=('Calibri', 11))
link_ent.grid(row=2, column=1, sticky='W', padx=5, pady=5)
#link_ent.insert(0,'https://smartbg.dynamics.bancogalicia.com.ar/apps/portal')

mail_ent = tk.Entry(ventana, textvariable = mail_var, width=60, font=('Calibri', 11))
mail_ent.grid(row=3, column=1, sticky='W', padx=5, pady=5)
#mail_ent.insert(0,'operador.galicia54@hotmail.com')

cont_ent = tk.Entry(ventana, textvariable = contrasena_var, width=60, font=('Calibri', 11), show="*")
cont_ent.grid(row=4, column=1, sticky='W', padx=5, pady=5)
#cont_ent.insert(0,'Oper1234')

ruta_origen_ent = tk.Entry(ventana, textvariable = ruta_origen_var, width=80, font=('Calibri', 11))
ruta_origen_ent.grid(row=6, column=1, sticky='W', padx=5, pady=5)

ruta_destino_ent = tk.Entry(ventana, textvariable = ruta_export_var, width=80, font=('Calibri', 11))
ruta_destino_ent.grid(row=7, column=1, sticky='W', padx=5, pady=5)

tiempo_ent = tk.Entry(ventana, textvariable = tiempo_var, width=80, font=('Calibri', 11))
tiempo_ent.grid(row=8, column=1, sticky='W', padx=5, pady=5)


def del_insert(objeto, insert):
    """Inserta texto en textbox previamente borra lo existente"""
    objeto.delete(0,'end')     
    objeto.insert(0, insert)


def leer_parametros():
    """lee los parametros en el archivo 'parametros.txt' para poder llenar los textbox con lo guardado"""
    with open('parametros.txt', 'r') as leer_param:
        parametros = leer_param.read()
        diccionario = ast.literal_eval(parametros)
    del_insert(link_ent,diccionario['link'])
    del_insert(mail_ent,diccionario['mail'])
    del_insert(cont_ent,diccionario['contrasena'])
    del_insert(ruta_origen_ent,diccionario['ruta origen'])
    del_insert(ruta_destino_ent,diccionario['ruta export'])
    del_insert(tiempo_ent,diccionario['tiempo'])


leer_parametros()

def crea_ventana_nueva():
    #Crear Ventana Pequeña
    print('crea ventana')
    ventana_pequeña = tk.Toplevel()
    ventana_pequeña.geometry('150x29')
    ventana_pequeña.configure(bg='#93BDA5')
    ventana_pequeña.overrideredirect(True)
    
    ventana_pequeña.resizable(width=False, height=False)



    

def ejecutar():
    """ejecuta el flujo del proceso. Construyendo"""
    #Abre chrome
    pantalla = gui.size()
    #crea_ventana_nueva()
    #Declaro Variables de archivos y lo asigno desde el front a Archivo_origen y Archivo destino
    global archivo_origen
    archivo_origen = ruta_origen_var.get()

    global archivo_destino
    archivo_destino = ruta_export_var.get()
    now = datetime.now()
    unique = now.strftime("%Y-%m-%d %H%M%S")
    print(f'unique:{unique}')
    #Leo Archivo origen
    with open(archivo_origen, 'r') as archivo:
        contenido = archivo.read().splitlines()

    global lista_dni
    #Vuelco Archivo origen en una lista de dnis
    lista_dni = list(contenido)
    print(f'lista_dni: {lista_dni}')

    contador_exito = 0

    contador_reintento = 0

    contador_reint_superado = 0

    contador_explor = 0
    resultado_exp = 'chrome no ejecuto'

    print('antes de ejecutar abrir chrome')
    time.sleep(2*tiempo_var.get())
    while resultado_exp == 'chrome no ejecuto' and contador_explor < 5:

        resultado_exp = abrir_explorador()
        print(f'resultado_exp:{resultado_exp}')
        

        if resultado_exp == "chrome ejecuto":

            abre_incognito()
            print('inicia proceso de abrir incognito')

            ingresa_smart(link_var.get())

            res_log = log_in(mail_var.get(), contrasena_var.get())
            print(res_log)
            if res_log == True:
                habilita_cursor()

                #Empieza el loop de pegado de dni
                #print(int(pantalla[0]*0.80),int(pantalla[1]*0.15), int(pantalla[0]*0.11), int(pantalla[1]*0.09))
                registro = 0
                for dni in lista_dni:
                    registro +=1
                    print(f'-------------------------registro: {registro}||{dni}---------------------------')
                    # Buscar personas
                    pag_buscar = busca_personas(pantalla, 0.001, 0.2777, 0.1010, 0.2529, 50)
                    print(f'pag buscar: {pag_buscar}')
                    if pag_buscar == 'buscar exitoso':
                        dni_current = busco_dni(dni)
                        cliente = copia_datos_dni(pantalla, dni_current)
                        print(f'Cliente: {cliente}')
                        if cliente != 'error al copiar datos del cliente':
                            nombre_cli, estado, sexo, fecha_nac_corr, dni_current = cliente
                            flujo = cli_activo(pantalla, estado)
                            print(f'Flujo:{flujo}')
                            if flujo == 'realizado':
                                verde = encontrar_verde(pantalla, estado)
                                print(f'verde: {verde}')
                                if verde != 'No se encuentra el punto verde':
                                    guardado = guarda_info(archivo_destino, dni_current, nombre_cli, estado, sexo, fecha_nac_corr, verde, unique)
                                    print(f'guardado: {guardado}')
                                    contador_exito +=1
                                else:
                                    guardado_else = guarda_info(archivo_destino, dni_current, nombre_cli, estado, sexo, fecha_nac_corr, 'n/c',unique)
                                    print(f'guardado_ else: {guardado_else}')
                                    reg_log(f'{archivo_destino}\log{date.today()}.txt',f'{verde}',dni_current)
                                    reintento_a = a_reintentar_dni(dni_current, archivo_origen, intentos=3)
                                    contador_reintento +=1
                                    if reintento_a != 'agregado':
                                       contador_reint_superado += 1 
                                    print(f'Rententar a: {reintento_a}')
                                    continue
                            else:
                                if cliente[1] == 'ACTIVO':
                                    guarda_info(archivo_destino, dni_current, nombre_cli, estado, sexo, fecha_nac_corr, 'n/c',unique)
                                    reg_log(f'{archivo_destino}\log{date.today()}.txt',f'{flujo}',dni_current)
                                    reintento_b = a_reintentar_dni(dni_current, archivo_origen, intentos=3)
                                    print(f'Rententar b: {reintento_b}')
                                    contador_reintento +=1
                                    if reintento_b != 'agregado':
                                        contador_reint_superado += 1
                                    continue
                                else:
                                    guarda_info(archivo_destino, dni_current, nombre_cli, estado, sexo, fecha_nac_corr, 'n/c',unique)
                                    reg_log(f'{archivo_destino}\log{date.today()}.txt',f'{flujo}',dni_current)
                                    continue
                        else:
                            #error al copiar datos del cliente 
                            
                            reg_log(f'{archivo_destino}\log{date.today()}.txt',f'{cliente}', dni_current)
                            continue
                    else:
                        #no encuentra buscar
                        reg_log(f'{archivo_destino}\log{date.today()}.txt',f'{pag_buscar}')
                        continue
            else:
                #Log in no se realizó
                reg_log(f'{archivo_destino}\log{date.today()}.txt',f'{res_log}')            
        else:
            #Chrome no ejecutó
            reg_log(f'{archivo_destino}\log{date.today()}.txt',f'{resultado_exp}')

    contador_explor +=1
    print(f'contador_explor: {contador_explor}')
    print(f'contador_exito: {contador_exito}')
    print(f'contador_reintento: {contador_reintento}')
    print(f'contador_reintento superado: {contador_reint_superado}')
#Frame




#Label
#Titulo
titulo_lb = tk.Label(ventana, text='SMART Test',font=('Calibri 18 bold'), foreground ='white',background='#377D56' ,relief=tk.GROOVE, bd=2, padx=10, pady=10, width='81')
titulo_lb.grid(row = 0, column=0, columnspan=4)

seccion_princ = tk.Label(ventana, text='Log-in',font=('Calibri 15 bold'), foreground ='#323133', background='#93BDA5')
seccion_princ.grid(row = 1, column=0, sticky='W', padx=5, pady=5)

link_lb = tk.Label(ventana, text='Link',font=('Calibri', 11), foreground ='#323133')
link_lb.grid(row = 2, column=0, sticky='W', padx=5, pady=5)

mail_lb = tk.Label(ventana, text='Mail',font=('Calibri', 11), foreground ='#323133')
mail_lb.grid(row = 3, column=0, sticky='W', padx=5, pady=5)

cont_lb = tk.Label(ventana, text='Contraseña',font=('Calibri', 11), foreground ='#323133')
cont_lb.grid(row = 4, column=0, sticky='W', padx=5, pady=5)

ruta_origen_lb = tk.Label(ventana, text='Ruta archivo origen',font=('Calibri', 11), foreground ='#323133')
ruta_origen_lb.grid(row = 6, column=0, sticky='W', padx=5, pady=5)

ruta_destino_lb = tk.Label(ventana, text='Ruta archivo destino',
                   font=('Calibri', 11), foreground ='#323133')
ruta_destino_lb.grid(row = 7, column=0, sticky='W', padx=5, pady=5)

tiempo_lb = tk.Label(ventana, text='Tiempo',
                   font=('Calibri', 11), foreground ='#323133')
tiempo_lb.grid(row = 8, column=0, sticky='W', padx=5, pady=5)

##Entry##



#separador1 = ttk.Separator(ventana, orient = 'horizontal')
#separador1.place(relx=0, rely=0.32, relwidth=1, relheight=1)

  
    

#Boton de ejecutar
botton_ejecutar = tk.Button(ventana, text='Iniciar', command=ejecutar, background='#377D56', font=('calibri',13), foreground='white')
botton_ejecutar.grid(row=10, column=2, padx=9, pady=9)

botton_ejecutar = tk.Button(ventana, text='Examinar', command=elegir_origen, background='#377D56', font=('calibri',12), foreground='white')
botton_ejecutar.grid(row=6, column=2, sticky='W')

botton_ejecutar = tk.Button(ventana, text='Examinar', command=elegir_destino, background='#377D56', font=('calibri',12), foreground='white')
botton_ejecutar.grid(row=7, column=2, sticky='W')

botton_ejecutar = tk.Button(ventana, text='Guardar', command=lambda:guardar(), background='#377D56', font=('calibri',12), foreground='white')
botton_ejecutar.grid(row=8, column=2, sticky='W')

#botton_ejecutar = tk.Button(ventana, text='tray', command=crea_ventana_nueva, background='#377D56', font=('calibri',13), foreground='white')
#botton_ejecutar.grid(row=11, column=2, padx=9, pady=9)



ventana.mainloop()
