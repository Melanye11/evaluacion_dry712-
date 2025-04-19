# verificación_puerto.py

print("=== VERIFICACIÓN DE PUERTOS ===")
print("------------------------------")

try:
    # Solicitar número de puerto al usuario
    puerto = int(input("Ingrese el número de puerto: "))
    
    # Verificar el rango del puerto
    if puerto >= 0 and puerto <= 1023:
        print(f"El puerto {puerto} es un PUERTO BIEN CONOCIDO (0-1023)")
    elif puerto >= 1024 and puerto <= 49151:
        print(f"El puerto {puerto} es un PUERTO REGISTRADO (1024-49151)")
    elif puerto >= 49152 and puerto <= 65535:
        print(f"El puerto {puerto} es un PUERTO DINÁMICO/PRIVADO (49152-65535)")
    else:
        print("¡Error! El número ingresado esta fuera de rango (0-65535)")
        
except ValueError:
    print("¡Error! Debe ingresar un número entero válido")

print("\nFin del programa")