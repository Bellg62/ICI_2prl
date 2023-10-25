#Escriba un dfd que dado el año de nacimiento indique cuántos años va a cumplir una persona el siguiente año.

from guizero import App, Text, TextBox,PushButton, Box

año_actual= 2023

def edad_prox():
    año_nacimiento = int(input_año_nacimiento.value)
    resultado.value = (f"Cumplirás: {año_actual - año_nacimiento + 1} años")
app = App(title="Calcular edad", layout="grid")
entrada_box = Box(app, layout="grid", grid=[0,0])
resultado = Text(app, text="",grid=[0, 1])
Text(entrada_box, text="Año de nacimiento:", grid=[0,1])
input_año_nacimiento = TextBox(entrada_box, grid=[1, 1])
calcular_button = PushButton(entrada_box, text="Calcular edad", grid=[0,2,2,1], command= edad_prox)
app.display()