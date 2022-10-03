#Importacion de bibliotecas
import RPi.GPIO as GPIO 
import time 
from datetime import datetime

#Configuracion de pines de entrada y salida
GPIO.setmode(GPIO.BCM) 
GPIO_TRIGGER = 23 
GPIO_ECHO    = 24 
GPIO.setup(GPIO_TRIGGER,GPIO.OUT) 
GPIO.setup(GPIO_ECHO,GPIO.IN) 
GPIO.output(GPIO_TRIGGER, False)

#Formato de fecha
sFileStamp = time.strftime('%Y%m%d%H') 

#Configuración de la variable para almacenar el nombre del archivo
sFileName = '\out' + sFileStamp + '.txt'
f=open(sFileName, 'a') 
f.write('TimeStamp,Value' + '\n') 

#Mensaje de inicio
print("Inicia la toma de datos")

#Uso de try para el manejo de errores
try: 
    while True:
        #Lectura del sensor
        GPIO.output(GPIO_TRIGGER,True) 
        time.sleep(0.00001) 
        GPIO.output(GPIO_TRIGGER,False) 
        start = time.time() 
        while GPIO.input(GPIO_ECHO)==0: 
            start = time.time() 
        while GPIO.input(GPIO_ECHO)==1: 
            stop = time.time() 
        elapsed = stop-start 
        distance = (elapsed * 34300)/2 

        #Guardado de datos en un archivo .txt
        sTimeStamp = time.strftime('%Y%m%d%H%M%S') 
        f.write(sTimeStamp + ',' + str(distance) + '\n') 
        print(sTimeStamp + ' ' + str(distance)) 
        time.sleep(1)

        #Procesos necesarios para el correcto almacenamiento
        if sTmpFileStamp != sFileStamp: 
           f.close 
           sFileName = 'out/' + sTmpFileStamp + '.txt' 
           f=open(sFileName, 'a') 
           sFileStamp = sTmpFileStamp 
           print ("creando el archivo")
        
except KeyboardInterrupt: 
    print ('\n' + 'termina la captura de datos.' + '\n') 
    f.close 
    GPIO.cleanup()