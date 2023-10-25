#Se desea saber la cantidad de alumnos que pasaron una materia, son 25 y la calificación aprobatoria es 7.

from guizero import App, TextBox, PushButton, Text
calificaciones = []
def contar_aprobados():
    try:
        calificaciones_str = entrada_calificacion.value.split()
        calificaciones_enteros = [float(calificacion) for calificacion in calificaciones_str]
        alumnos_aprobados = sum(1 for calificacion in calificaciones_enteros if calificacion >= 7)
        resultado.value = "Alumnos que aprobaron: {}".format(alumnos_aprobados)
    except ValueError:
        resultado.value = "Por favor, ingrese calificaciones válidas."
def agregar_calificacion():
    try:
        calificacion = float(entrada_calificacion.value)
        calificaciones.append(calificacion)
        entrada_calificacion.clear()
        resultado.value = ""  
    except ValueError:
        resultado.value = "Por favor, ingrese una calificación válida"
app = App("Contador de Alumnos Aprobados", width=300, height=200)
texto_instrucciones = Text(app, text="Ingrese las calificaciones de los alumnos separadas por espacios:")
entrada_calificacion = TextBox(app, width=40)
boton_contar = PushButton(app, text="Contar Aprobados", command=contar_aprobados)
resultado = Text(app, text="Resultado aparecerá aquí.")
app.display()
