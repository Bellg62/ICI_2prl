#Escriba un dfd que calcule el cuadrado de un número positivo leído desde el teclado.

from guizero import App, Text, TextBox,PushButton
def generar_cuadrado():
    cuadrado = str(int(name.value)**2)
    message.value = f"El cuadrado del número es: {cuadrado}"
app = App(title="Calcular cuadrado")
message = Text(app, text="Dame un número")
name = TextBox(app, width= 20)
cuadrado_button = PushButton(app, text="Calcular cuadrado", command= generar_cuadrado)
message_cuadrado = Text(app, text= "")
app.display()