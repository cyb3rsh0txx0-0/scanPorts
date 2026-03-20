import socket 
from concurrent.futures import ThreadPoolExecutor
import subprocess

obj=input('Ingrese el objetivo  a escanear :')
TARGET=obj

des=int(input('Ingrese el puerto desde donde quiere empezar el escaneo : '))
has=int(input('Ingrese el puerto hasta quiere terminar el escaneo : '))

PORTS=range(des,has)

puertos=[]
def portSC(puerto):
        try:
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((TARGET,puerto))
            print('---PUERTOS ABIERTOS----\n')
            print(f'open port {puerto} \n')
            print('-----------------------')
            puertos.append(puerto)
        except:
            pass

with ThreadPoolExecutor(max_workers=500) as ejecutor:
     ejecutor.map(portSC,PORTS)

infoport=input('Desea ver que estan escuchando los puertos escaneados ? [S/N]').lower()
for p in puertos:
        if infoport =='s':
            subprocess.run(['lsof','-i',f':{p}'])