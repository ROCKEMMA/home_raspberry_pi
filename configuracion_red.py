# configuracion_red.py
import network
import time
from machine import Pin

def conectar_wifi(lista_redes):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    # Desconectar primero si estaba conectado
    if wlan.isconnected():
        wlan.disconnect()
    
    for red in lista_redes:
        print(f"\nIntentando conectar a: {red['ssid']}...")
        wlan.connect(red['ssid'], red['password'])
        
        timeout = 0
        while not wlan.isconnected() and timeout < 10:
            print(".", end="")
            time.sleep(1)
            timeout += 1
        
        if wlan.isconnected():
            ip, netmask, gateway, dns = wlan.ifconfig()
            
            print("\n\n--- Conexión Exitosa ---")
            print(f"Red:           {red['ssid']}")
            print(f"IP:            {ip}")
            print(f"Máscara:       {netmask}")
            print(f"Gateway:       {gateway}")
            print(f"DNS:           {dns}")
            print("------------------------")
            
            # Feedback visual
            indicador_conexion_exitosa()
            return True
    
    print("\nError: No se pudo conectar a ninguna red")
    indicador_error_conexion()
    return False

def indicador_conexion_exitosa():
    led = Pin("LED", Pin.OUT)
    # 3 parpadeos rápidos
    for _ in range(3):
        led.on()
        time.sleep(0.15)
        led.off()
        time.sleep(0.15)
    led.on()  # Permanecer encendido

def indicador_error_conexion():
    led = Pin("LED", Pin.OUT)
    # 5 parpadeos lentos
    for _ in range(5):
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)