#Calcular la edad de una persona tomando el año de nacimiento y el año actual.

from guizero import App, Box, Text, TextBox, PushButton

def calcular_edad():
    año_actual = int(input_año_actual.value)
    año_nacimiento = int(input_año_nacimiento.value)
    resultado.value = (f"Edad:{año_actual - año_nacimiento} años")
app = App(title="Calcular edad", layout="grid")
entrada_box = Box(app, layout="grid", grid=[0,0])
resultado = Text(app, text="",grid=[0, 1])
Text(entrada_box, text="Año actual:", grid=[0,0])
input_año_actual = TextBox(entrada_box,grid=[1,0])
Text(entrada_box, text="Año de nacimiento:", grid=[0,1])
input_año_nacimiento = TextBox(entrada_box, grid=[1, 1])
calcular_button = PushButton(entrada_box, text="Calcular edad", grid=[0,2,2,1], command=calcular_edad)
app.display()