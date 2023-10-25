#Genera la siguiente secuencia 01010101...

from guizero import App, Text, TextBox,PushButton

def secuencia():
    rp= int(entrada_rp.value)
    if rp < 1:
        message.value= Text(app, text="Ingresa un número mayor a 1")
        entrada_rp.value = ""
        return
    sequence = "".join("01"[i % 2] for i in range(rp))
    message.value = f"La suma de los números es: {sequence}"


app = App("Generador secuencia")


Text(app, "Ingrese cantidad de números que quiere:")
entrada_rp = TextBox(app,"")
message = Text(app)
button = PushButton(app, text="Crear secuencia", command= secuencia)
app.display()
