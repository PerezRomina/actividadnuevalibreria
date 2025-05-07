import tkinter as tk

ventana = tk.Tk()
ventana.title("Rpmina Odalys Perez Mendez")
ventana.geometry("700x400")
ventana.config(bg="lightblue")
etiqueta_nombre = tk.Label(ventana, text="Introduce tu nombre:")
etiqueta_nombre.pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

etiqueta_genero=tk.Label(ventana, text="Introduce tu género")
etiqueta_genero.pack()
entrada_genero=tk.Entry(ventana)
entrada_genero.pack()

etiqueta_nacionalidad=tk.Label(ventana, text="Introduce tu nacionalidad")
etiqueta_nacionalidad.pack()
entrada_nacionalidad=tk.Entry(ventana)
entrada_nacionalidad.pack()

etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()
def saludar():
 nombre=entrada_nombre.get()
 genero=entrada_genero.get()
 nacionalidad=entrada_nacionalidad.get()
 etiqueta_resultado.config(text=f"Buen dia {nombre},Somos del hospital, y se registró que su género es {genero} y que su nacionalidad es {nacionalidad}")
boton_saludar= tk.Button(ventana, text="Clic para registrarse", command=saludar)
boton_saludar.pack()
ventana.mainloop()
