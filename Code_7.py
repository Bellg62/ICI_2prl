from guizero import App, TextBox, PushButton, Text

numeros = []
def calcular_suma():
    suma_cuadrados_pares = 0
    suma_cubos_impares = 0
    try:
        numeros_str = entrada_num.value.split()
        numeros_enteros = [int(numero) for numero in numeros_str if int(numero) > 0]
        for numero in numeros_enteros:
            if numero % 2 == 0:
                suma_cuadrados_pares += numero ** 2
            else:
                suma_cubos_impares += numero ** 3
        resultado.value = "Suma cuadrados pares: {}\n, Suma cubos impares: {}".format(suma_cuadrados_pares, suma_cubos_impares)
    except ValueError:
        resultado.value = "Por favor, ingrese números positivos válidos."
def agregar_numero():
    try:
        numero = int(entrada_numero.value)
        numeros.append(numero)
        entrada_numero.clear()
        resultado.value = ""  
    except ValueError:
        resultado.value = "Por favor, ingrese un número positivo válido."
app = App("Suma_pares, cubo_impares", width=300, height=200)
texto_instrucciones = Text(app, text="Ingrese números positivos separados por espacios:")
entrada_num = TextBox(app, width=40)  
boton_calcular = PushButton(app, text="Calcular Suma", command=calcular_suma)
resultado = Text(app, text="Resultado aparecerá aquí.")
app.display()