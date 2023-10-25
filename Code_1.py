#Obtenga el promedio de tres números cualquiera

from guizero import App, Text, TextBox,PushButton
import pyttsx3
engine = pyttsx3.init()
def calcular_promedio():
    resultado = int(name.value)
    resultado_2 = int(name_2.value)
    resultado_3 = int(name_3.value)
    suma =int(resultado + resultado_2 + resultado_3)
    cadena = f"El promedio de los números es {suma / 3}"
    engine.say(cadena)
    engine.runAndWait()
app = App(title="Calcular promedio")
message = Text(app, text="Dame un número")
name = TextBox(app, width=20)
message_2 = Text(app, text="Dame un segundo número")
name_2 = TextBox(app, width=20)
message_3 = Text(app, text="Dame un  tercer número")
name_3 = TextBox(app, width=20)
button = PushButton(app, text="Calcular promedio", command= calcular_promedio)
mensaje_promedio= Text(app, text="")
app.display()