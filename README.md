🛡️ Generador de Contraseñas Criptográficamente Seguras (Python)
Este proyecto es una implementación en Python de una herramienta esencial de ciberseguridad personal: un generador de contraseñas robustas. El objetivo es producir strings altamente aleatorios e impredecibles, adhiriéndose a las mejores prácticas de seguridad.

🌟 Características Clave
Longitud Mínima Reforzada: Impone una longitud mínima de 20 caracteres por defecto. Esta longitud extrema maximiza la entropía y ofrece una resistencia superior contra ataques de fuerza bruta.

Aleatoriedad Criptográficamente Fuerte: Utiliza el módulo secrets de Python, asegurando que la generación de la contraseña sea resistente a ataques de predicción.

Garantía de Diversidad: El algoritmo asegura que cada contraseña contenga al menos una Mayúscula, una Minúscula, un Número y un Símbolo, incrementando su complejidad de manera determinística.

Usabilidad: Interfaz de consola sencilla que solicita al usuario la longitud deseada.

🛠️ Tecnologías Utilizadas
Lenguaje: Python 3.x

Módulos:

secrets: Utilizado para todas las elecciones aleatorias críticas.

string: Proporciona conjuntos de caracteres estandarizados (letras, dígitos, puntuación).

random: Se utiliza de forma segura únicamente para la función de barajado (random.shuffle), asegurando que la posición de los caracteres garantizados sea aleatoria.


Posibles Mejoras Futuras
Argumentos de Línea de Comandos: Implementar el módulo argparse para permitir al usuario especificar la longitud y el conjunto de caracteres sin interacción por input().

Evaluación de Fuerza (Entropy Score): Integrar una librería como Zxcvbn para proporcionar una métrica de la fuerza de la contraseña generada.
