import os

env = os.getenv("APP_ENV", "qa").lower()
nombre = os.getenv("NOMBRE", "invitado")
debug = os.getenv("DEBUG", "false").lower()
version= os.getenv("VERSION", "1.0")

print(f"Hola {nombre}")
print(f"Entorno: {env}")
print(f"Version: {version}")

if env=="prod":    
    print(f"Modo seguro activado")
    debug="false"
elif env== "qa":
    print(f"Modo testing activado")

else:
    print("⚠️ Entorno no reconocido → modo no productivo")
    print("Modo testing activado (fallback)")

if debug == "true":
    print("DEBUG ACTIVADO")
    print("Mostrando información interna...")
    