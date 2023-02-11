import pandas as pd
import os
import db
message="""
    1)Insertar data:
    2)Actualizar data del dolar
"""
print(message)
a=int(input('ingrese la tarea a realizar: '))

def insertData():
    #obtiene la ruta absoluta
    path_=os.getcwd()+'\dataTienda.csv'
    #conection a bd
    conn=db.Conection('tienda.db')
    cursor=conn.getCursor()
    print(path_)
    df = pd. read_csv (path_, sep = ";") 
    ### logica para insertar 
    for i,fila in df.iterrows():
        print(fila['ORDER_ID'])

def updateDolar():
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat' #tipo cambio sunat
    pass
try:
    if a == 1:
        insertData()
except:
    pass



