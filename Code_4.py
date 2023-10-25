#Quiero obtener la edad promedio de N personas preguntandoles su año de nacimiento y asumiendo que el año actual es 2023.

from guizero import App, TextBox, PushButton, Text

años_de_nacimiento = []

def calcular_edad_promedio():
    try:
        total_años = 0
        for año in años_de_nacimiento:
            total_años += 2023 - int(año)
        if total_años > 0:
            edad_promedio = total_años / len(años_de_nacimiento)
            resultado.value = "Edad promedio: {:.2f}".format(edad_promedio)
        else:
            resultado.value = "Por favor, ingrese años de nacimiento válidos."
    except ValueError:
        resultado.value = "Por favor, ingrese años de nacimiento válidos."

def agregar_año_de_nacimiento():
    año = entrada_año.value
    años_de_nacimiento.append(año)
    entrada_año.clear()

app = App("Calculadora de Edad Promedio", width=300, height=200)
texto_instrucciones = Text(app, text="Ingrese el año de nacimiento:")
entrada_año = TextBox(app)
boton_agregar = PushButton(app, text="Agregar", command=agregar_año_de_nacimiento)
resultado = Text(app, text="Edad promedio: ")

button = PushButton(app, text="Calcular", command=calcular_edad_promedio)

app.display()
