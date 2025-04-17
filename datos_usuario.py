# datos_usuario.py
# Script básico para solicitar y mostrar información del usuario

print("=== DATOS DEL USUARIO ===")
print("-------------------------")

# Solicitar información al usuario
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
codigo_seccion = input("Ingrese su código-sección: ")
sede = input("Ingrese su sede: ")

# Mostrar información formateada
print("\n--- Información ingresada ---")
print(f"Nombre: {nombre}")
print(f"Apellido: {apellido}")
print(f"Código-Sección: {codigo_seccion}")
print(f"Sede: {sede}")

print("\nGracias por ingresar tus datos!")