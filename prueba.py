import re
def validar_monto(monto):
    patron = r'^[0-9]+$'
    if re.match(patron, monto):
        return monto
    else:
        return 'monto erroneo'    
    
monto0 = '363900'
monto1 = validar_monto(monto0)
print(monto1)