from requests_ppm import *
import time


def dataInternetInterfaceCronDetail():
    print('Creando reporte ... Por favor esperar')
    inicio = time.strftime("%c")
    print("Fecha y hora de inicio: "+time.strftime("%c"))
    dataInternetInterface()
    fin = time.strftime("%c")
    print("Inicio: "+str(inicio)+" - Fin: "+str(fin))
    print("Reporte completo!!! :D")
