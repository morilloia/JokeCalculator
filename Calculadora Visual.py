import tkinter as tk
def calculadoraSuma():
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        resultado = n1 + n2
        resultado_label.config(text=f"EL RESULTADO ES: {resultado}")
    except ValueError:
        resultado_label.config(text="INGRESA NÚMEROS VÁLIDOS")
def calculadoraResta():
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        resultado = n1 - n2
        resultado_label.config(text=f"EL RESULTADO ES: {resultado}")
    except ValueError:
        resultado_label.config(text="INGRESA NÚMEROS VÁLIDOS")
def calculadoraMultipl():
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        resultado = n1 * n2
        resultado_label.config(text=f"EL RESULTADO ES: {resultado}")
    except ValueError:
        resultado_label.config(text="INGRESA NÚMEROS VÁLIDOS")
def calculadoraDiv():
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        if n2 == 0:
            resultado_label.config(text="NO PUEDES DIVIDIR ENTRE 0")
        else:
            resultado = n1 / n2
            resultado_label.config(text=f"EL RESULTADO ES: {resultado}")
    except ValueError:
        resultado_label.config(text="INGRESA NÚMEROS VÁLIDOS")

mainWindow = tk.Tk()
mainWindow.title("TITULOS")
mainWindow.geometry("800x500")
mainWindow.minsize(500,300)
mainWindow.configure(bg="black")

tk.Label( #TITULO
    mainWindow,
    text="CALCULADORA SIMPLE",
    font=("Comic Sans MS", 20),
    fg="yellow",
    bg="black", 
    ).pack()

tk.Label(mainWindow, 
    text="NUMERO 1",
    font=("Comic Sans MS", 15),
    bg="black",
    fg="yellow").pack()
entrada1 = tk.Entry( #el input1(numero1), básicamente
    mainWindow,
    width=35,
    border= 22,
    bg="yellow",
    fg="black",
    font=("Comic Sans MS", 13,"bold")
)
entrada1.pack()

num2 = tk.Label(mainWindow,
    text="NUMERO 2",
    font=("Comic Sans MS", 15),
    bg="black",
    fg="yellow").pack()
entrada2 = tk.Entry( #El input2(numero2), básicamente
    mainWindow,
    width=35,
    border= 22,
    bg="yellow",
    fg="black",
    font=("Comic Sans MS", 13,"bold")
)
entrada2.pack()
frame_botones = tk.Frame(mainWindow)
botonsuma = tk.Button(frame_botones,text="SUMAR",bg="yellow",fg="black",font=("Comic Sans MS", 10,"bold",),width=15,command=calculadoraSuma,padx=5).pack(side=tk.LEFT)
botonresta = tk.Button(frame_botones,text="RESTAR",bg="yellow",fg="black",font=("Comic Sans MS", 10,"bold",),width=15,padx=5,command=calculadoraResta).pack(side=tk.LEFT)
botonmultiplicacion = tk.Button(frame_botones,text="MULTIPLICAR",bg="yellow",fg="black",font=("Comic Sans MS", 10,"bold",),padx=5,width=15,command=calculadoraMultipl).pack(side=tk.LEFT)
botondividir = tk.Button(frame_botones,text="DIVIDIR",bg="yellow",fg="black",font=("Comic Sans MS", 10,"bold"),width=15,padx=5,command=calculadoraDiv).pack(side=tk.LEFT)
frame_botones.pack(side=tk.TOP,pady=50)



resultado_label = tk.Label(mainWindow,text="RESULTADO: ",
    font=("Comic Sans MS", 20),
    fg="yellow",
    bg="black",
)
resultado_label.pack()
mainWindow.mainloop()