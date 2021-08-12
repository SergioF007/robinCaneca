#sudo apt-get install python3-serial  ó pip install serial
import serial
import os
#import Arduino~
#sudo apt-get  install python3-pandas
import pandas as pd
#sudo apt-get install csv python3  ó  sudo pip3 install python-csv
import csv
#sudo apt-get  install python3-numpy
import numpy as np
from time import strftime, localtime, asctime

from datetime import time as tm
from datetime import datetime, date, timedelta
#	sudo apt install python3-picamera
#from picamera import PiCamera
from time import sleep
arduino = serial.Serial('/dev/ttyUSB0',9600)  
arduino.setDTR(False)
sleep(1)
arduino.flushInput()
arduino.setDTR(True)
c = []
i = []
u = []
p = []
t = []
nombre = []
material = []
nombreA=asctime(localtime())
     
try:
  while True:
     lineBytes = arduino.readline()
     line = lineBytes.decode('utf-8').strip()
     print(line)
     # Separamos los datos recibidos mediante el seprador "|"
     #capacitivo, inductivo, ultrasonico, peso, sFin = line.split("|", 4) 
     s1,s2,s3,s4,sFin = line.split("|", 4)    
     capacitivo = s1
     inductivo = s2
     ultrasonico =s3
     peso = s4 
     c.append(int(capacitivo))
     i.append(int(inductivo)) 
     u.append(int(ultrasonico))
     p.append (float(peso))
     t.append(strftime("%H:%M:%S")) # %Y-%m-%d 
     print("nombre")
     nombre.append(str(input()))
     #nombre = input('nombre: ')
     print("material")
     material.append(str(input()))
     #material = input('nombre: ')
     tiempo=np.array(t)
     sensor1=np.array(c)
     sensor2=np.array(i)
     sensor3=np.array(u)
     sensor4=np.array(p)
     nombreObjeto=np.array(nombre)
     tipoMaterial=np.array(material)
     data={'tiempo': tiempo,'Capacitivo': sensor1, 'inductivo': sensor2, 'ultrasonico': sensor3, 'peso': sensor4, 'nombreObjeto': nombre, 'tipoMaterial': material }
     df=pd.DataFrame(data)
     print(df)
     df.to_csv(str(nombreA)+"-MatrizSensores.csv")
     #df.to_excel(nombreArchivo+"Matriz.xlsx")
     #este dato de posicion depende de la clasificacion de que material es
     comando = input('ingresa posicion del motor: ')
     arduino.write(comando.encode())


except KeyboardInterrupt:
	os.system('clear')
	print
	print("Programa Terminado por el usuario")
	print
	exit()
