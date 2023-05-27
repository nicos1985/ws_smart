import datetime
import time
contador_exito = 50
contador_reintento = 5
contador_reint_superado = 2
now = datetime.datetime.now()

unique = now.strftime("%Y-%m-%d %H%M%S") 
time.sleep(5)
now_fin = datetime.datetime.now()
unique_fin = now_fin.strftime("%Y-%m-%d %H%M%S")
print(f'unique_fin: {unique_fin}')
diferencia = datetime.datetime.strptime(unique_fin, "%Y-%m-%d %H%M%S") - datetime.datetime.strptime(unique, "%Y-%m-%d %H%M%S")
print(f'diferencia: {diferencia}')
# Convierte la diferencia en horas y minutos
diferencia_horas = diferencia.seconds // 3600
print(f'diferencia_horas: {diferencia_horas}')
diferencia_minutos = (diferencia.seconds % 3600) // 60
print(f'diferencia_minutos: {diferencia_minutos}')
segundos = diferencia.seconds
print(f'segundos: {segundos}')
total_dni = contador_exito+contador_reintento+contador_reint_superado
prom_por_dni = round((segundos / total_dni),1)
print(f'prom_por_dni: {prom_por_dni}')
# Imprime la diferencia en horas y minutos
print(f'Proceso Finalizado: \nInicio de Proceso: {unique}\nFin de proceso: {unique_fin}\nTiempo total: {diferencia_horas}hs : {diferencia_minutos} min\n DNI Exitosos: {contador_exito},\n DNI Reintentados: {contador_reintento},\n DNI Reintentos superados: {contador_reint_superado}\n Total Procesos: {total_dni}\n Promedio de tiempo por DNI: {prom_por_dni} seg.')