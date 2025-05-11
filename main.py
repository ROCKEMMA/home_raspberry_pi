from machine import Pin
from time import sleep

from configuracion_red import conectar_wifi

LED = Pin(15, Pin.OUT)
try:
    while True:
        LED.on()     # Encender
        print("LED ENCENDIDO")
        sleep(1)     # Espera 1 segundo
        #LED.off()    # Apagar
        #print("LED APAGADO")
        #sleep(1)
        
except KeyboardInterrupt:
    LED.off()  # Apagar al detener el programa
    print("\nPrueba finalizada")


REDES = [
    {'ssid': 'Turbonet.2', 'password': 'T-FORCErm'},
    {'ssid': 'iphone', 'password': 'rm123456'}
]

if conectar_wifi(REDES):
    print("Conectado a WiFi - Ejecutando programa principal")
else:
    print("Modo offline - Funcionalidades limitadas")
    