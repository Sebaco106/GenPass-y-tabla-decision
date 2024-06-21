import re

def verificar_contrasena(contrasena):
    # 1. Longitud entre 8 y 10 caracteres
    if not (8 <= len(contrasena) <= 10):
        return "La contraseña debe tener entre 8 y 10 caracteres."
    
    # 2. Contiene al menos 2 letras
    if len(re.findall(r'[a-zA-Z]', contrasena)) < 2:
        return "La contraseña debe contener al menos 2 letras."
    
    # 3. Contiene al menos una letra mayúscula
    if not any(c.isupper() for c in contrasena):
        return "La contraseña debe contener al menos una letra mayúscula."
    
    # 4. Contiene al menos una letra minúscula
    if not any(c.islower() for c in contrasena):
        return "La contraseña debe contener al menos una letra minúscula."
    
    # 5. Contiene al menos un dígito
    if not any(c.isdigit() for c in contrasena):
        return "La contraseña debe contener al menos un dígito."
    
    # 6. Contiene al menos un carácter especial
    if not any(c in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~" for c in contrasena):
        return "La contraseña debe contener al menos un carácter especial."
    
    # Si cumple todas las condiciones
    return "La contraseña cumple con todos los requisitos."

def pedir_contrasena():
    while True:
        contrasena = input("Ingrese su contraseña (debe tener entre 8 y 10 caracteres, al menos 2 letras, "
                           "1 mayúscula, 1 minúscula, 1 número y 1 carácter especial): ")

        resultado = verificar_contrasena(contrasena)
        if resultado == "La contraseña cumple con todos los requisitos.":
            print("¡Contraseña válida! ✔️")
            break
        else:
            print(f"La contraseña no cumple con los requisitos: {resultado}. Inténtelo nuevamente.\n")

if __name__ == "__main__":
    print("Bienvenido al creador de contraseñas seguras.")
    pedir_contrasena()
