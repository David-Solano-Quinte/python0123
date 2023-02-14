import pandas as pd
import os
import db
import requests
from lxml import html
from csv import writer
from csv import reader
import matplotlib as plt

message="""
    1)Insertar data:
    2)Actualizar data del dolar
    3)Mostrar grafico del dolar
    4)Buscar un producto
    0)Salir
"""
def insertData():
    #obtiene la ruta absoluta
    path_=os.getcwd()+'\project\dataTienda.csv'
    #conection a bd
    conn=db.Conection('tienda.db')
    cursor=conn.getCursor()
    print(path_)
    df = pd. read_csv (path_, sep = ";") 
    ### logica para insertar 
    """for i,fila in df.iterrows():
        print(fila['ORDER_ID'])"""
    
    with open (path_,"a",newline="") as data_t:
        new_data=[]
        new_v= list (df.columns.values)
        for a in new_v :
            new_data.append(input(f"Ingrese el valor de {a}:"))
        writer_obj = writer(data_t)
        writer_obj.writerow(b for b in new_data)
        data_t.close()
def updateDolar():
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat' #tipo cambio sunat
    response = requests.get(url)
    data = response.json()
    data_venta = data["venta"]
    data_fecha = data["fecha"]
    update = {"Precio":data_venta,"Fecha":data_fecha}
    with open ("Historico_Dolar.csv", 'a',newline="",) as hd:
        writer_obj = writer(hd)
        writer_obj.writerow(update.values())
        hd.close()
def grafDolar():
    datos_graf = pd.read_csv("Historico_Dolar.csv",header=0,sep=",") 
    grafico= datos_graf[["Precio", "Fecha"]]
    print (grafico)
    ax = grafico.plot.bar(x="Precio",y="Fecha",rot=0)

    x_fecha = grafico['Fecha']
    y_precio  = grafico['Precio']
    plt.plot(x_fecha,y_precio,'*')
    plt.title('Historico del dolar')
    plt.grid()
    plt.show()
def buscar_producto():
    path_=os.getcwd()+'\project\dataTienda.csv'
    df = pd. read_csv (path_,header=0, sep = ";")
    plb_busc = input("Ingrese el producto a buscar: ")
    condicion=(df["NAME"]==plb_busc.upper())
    print(df[condicion])
    """columna_productos=df["NAME"]
    lista_productos = list(columna_productos.values)
    ubi = []
    a=int(0)
    for producto in lista_productos:
        if plb_busc.lower() == producto.lower():
            ubi.append(a)
        a+=1
    print (ubi)"""
while True:
    try:
        print(message)
        a=int(input('ingrese la tarea a realizar: '))
        if a == 1:
            insertData()
        elif a==2:
            updateDolar()
        elif a==3:
            grafDolar()
        elif a ==4:
            buscar_producto()
        elif a==0:
            break
    except:
        print ("error")



