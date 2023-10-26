import tkinter as tk

def calcular():
    """En esta funcion estará todo lo relacionado con la calculadora, luego se puede refactorizar"""
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operacion = operacion_var.get()
    if operacion == "Suma":
        resultado = num1 + num2
    elif operacion == "Resta":
        resultado = num1 - num2
    else:
        resultado = "Operación no válida"
        
    label_resultado.config(text="Resultado: " + str(resultado))    

    