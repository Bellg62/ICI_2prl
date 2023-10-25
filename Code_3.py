from guizero import App, Text, TextBox, PushButton

import pyttsx3

engine = pyttsx3.init()

suma = 0
contador = 0
cantidad_numeros = 0
numeros_ingresados = []

def set_cantidad():
    global cantidad_numeros
    try:
        cantidad_numeros = int(input_cantidad.value)
        input_cantidad.disable()
        engine.say(f"Se ingresarán {cantidad_numeros} números.")
        engine.runAndWait()
    except ValueError:
        engine.say("Por favor, ingresa una cantidad válida.")
        engine.runAndWait()

def ingresar_numero():
    global suma, contador, cantidad_numeros
    try:
        if contador < cantidad_numeros:
            num = float(input_numero.value)
            suma += num
            contador += 1
            numeros_ingresados.append(num)
            input_numero.clear()
            engine.say(f"Número {num} ingresado.")
            engine.runAndWait()
        else:
            engine.say("Ya has ingresado la cantidad de números especificada.")
            engine.runAndWait()
    except ValueError:
        engine.say("Por favor, ingresa un número válido.")
        engine.runAndWait()

def mostrar_numeros():
    numeros_texto = ", ".join(map(str, numeros_ingresados))
    engine.say(f"Números ingresados: {numeros_texto}")
    engine.runAndWait()

def calcular_promedio():
    if contador == cantidad_numeros:
        promedio = suma / contador
        engine.say(f"El promedio de los números ingresados es {promedio}")
        engine.runAndWait()
    else:
        engine.say("Por favor, asegúrate de ingresar la cantidad correcta de números.")
        engine.runAndWait()

app = App("Obtener Promedio de N Números")

Text(app, text="Ingrese la cantidad de números:")
input_cantidad = TextBox(app, width=5)

boton_set_cantidad = PushButton(app, text="Establecer Cantidad", command=set_cantidad)

Text(app, text="Ingrese un número:")
input_numero = TextBox(app, width=5)

boton_ingresar = PushButton(app, text="Ingresar", command=ingresar_numero)
boton_ver_numeros = PushButton(app, text="Ver Números Ingresados", command=mostrar_numeros)
boton_calcular = PushButton(app, text="Calcular Promedio", command=calcular_promedio)

app.display()
