#Proyectito Creado por Diego Paillalef 🐱
import string
import secrets #Modulo preferido por la Seguridad de las contraseñas enfocado en el area de la criptografia y era
import random # Se usa solo para la función de barajado final 

def generar_contraseña_segura():
    """
    Genera una contraseña fuerte y criptográficamente segura.
    Asegura la inclusión de al menos una minúscula, mayúscula, dígito y símbolo.
    """
    # 1. Definición de conjuntos de caracteres
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_chars = lower + upper + digits + symbols
    
    # 2. Entrada de usuario con validación de longitud
    MIN_LENGTH =18

    try:
        # Pide la longitud y valida que sea un número entero
        longitud = int(input(f"Ingrese el tamaño de su contraseña (mínimo {MIN_LENGTH}): "))
    except ValueError:
        print(" Error: Por favor, ingrese solo números enteros.")
        return

    while longitud < MIN_LENGTH:
        print(f"¡Error! La contraseña debe tener al menos {MIN_LENGTH} caracteres para ser segura ponte serio sielvo.")
        try:
            longitud = int(input("Ingrese el tamaño de su contraseña: "))
        except ValueError:
            print(" Error: Por favor, ingrese solo números enteros.")
            return

    # 3. Asegurar la inclusión de todos los tipos de caracteres
    password_list = []

    # Garantiza al menos una ocurrencia de cada tipo utilizando 'secrets'
    password_list.append(secrets.choice(lower))
    password_list.append(secrets.choice(upper))
    password_list.append(secrets.choice(digits))
    password_list.append(secrets.choice(symbols))

    # Rellena el resto de la longitud con una mezcla aleatoria
    # Esto usa (longitud - 4) porque ya agregamos 4 caracteres obligatorios
    for _ in range(longitud - 4):
        password_list.append(secrets.choice(all_chars))

    # 4. Barajar la lista para aleatorizar la posición de los caracteres garantizados
    # Nota: random.shuffle es seguro para este propósito, ya que solo reordena
    random.shuffle(password_list)

    # 5. Convertir la lista a cadena (string)
    contraseña = "".join(password_list)

    print("\n---")
    print(f"✅ Longitud solicitada: {longitud}")
    print(" Contraseña generada es: **" + contraseña + "**")
    print("---")


if __name__ == "__main__":
    generar_contraseña_segura()