import network
import time
from machine import Pin

def conectar_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    print(f"Conectando a la red: {ssid}...")
    wlan.connect(ssid, password)
    
    timeout = 0
    while not wlan.isconnected() and timeout < 10:
        print("Esperando conexión...")
        time.sleep(1)
        timeout += 1
    
    if wlan.isconnected():
        ip, netmask, gateway, dns = wlan.ifconfig()
        
        print("\n--- Configuración de Red ---")
        print(f"Dirección IP:      {ip}")
        print(f"Máscara de red:    {netmask}")
        print(f"Puerta de enlace:  {gateway}")
        print(f"Servidor DNS:      {dns}")
        print("---------------------------")
        
        # LED
        led = Pin("LED", Pin.OUT)
        led.on()
        time.sleep(3)
        led.off()
    else:
        print("\nError: No se pudo conectar. Revisa SSID/contraseña.")