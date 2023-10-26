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
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Básica")

# Crear etiquetas
label_num1 = tk.Label(ventana, text="Número 1:")
label_num2 = tk.Label(ventana, text="Número 2:")
label_operacion = tk.Label(ventana, text="Operación:")
label_resultado = tk.Label(ventana, text="Resultado:")

label_num1.pack()
label_num2.pack()
label_operacion.pack()

# Crear campos de entrada
entry_num1 = tk.Entry(ventana)
entry_num2 = tk.Entry(ventana)

entry_num1.pack()
entry_num2.pack()

# Crear variable de opción para la operación
operacion_var = tk.StringVar()
operacion_var.set("Suma")  # Valor predeterminado

# Crear botones de opción para la operación
suma_radio = tk.Radiobutton(ventana, text="Suma", variable=operacion_var, value="Suma")
resta_radio = tk.Radiobutton(ventana, text="Resta", variable=operacion_var, value="Resta")

suma_radio.pack()
resta_radio.pack()

# Crear botón para calcular
calcular_button = tk.Button(ventana, text="Calcular", command=calcular)
calcular_button.pack()

label_resultado.pack()

ventana.mainloop()   

    