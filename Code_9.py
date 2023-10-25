#Obtenga la suma de 5 números capturados [5,10]

from guizero import App, Text, TextBox,PushButton
def calcular_suma():
    numeros_str = entrada_numeros.value.split()
    numeros_enteros = [int(numero) for numero in numeros_str]
    for numero in numeros_enteros:
        if numero < 5 or numero > 10:
             resultado.value = "Por favor, ingrese números en el rango de 5 a 10."
             return
    suma = sum(numeros_enteros)
    resultado.value = "Suma de los números: {}".format(suma)
def new_num():
    numero = int(entrada_numero.value)
    numeros.append(numero)
    entrada_numero.clear()
    resultado.value = ""
    if len(numeros) == 5:
            boton_calcular.enable()
    message.value = Text(app, text=f"La suma de los números es: {suma}")
app = App("Suma de 5 núm. entre 5,10")
message = Text(app, text="Ingrese 5 números en el rango de 5 a 10, separados por espacios:")
entrada_numeros = TextBox(app, width=20)  
boton_calcular = PushButton(app, text="Calcular Suma", command=calcular_suma)
resultado = Text(app, text="")
app.display()