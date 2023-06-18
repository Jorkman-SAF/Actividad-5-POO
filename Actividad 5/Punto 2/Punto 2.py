import tkinter as tk
import math

class VentanaPrincipal:
    def __init__(self, ventana):
        self.ventana = ventana

        self.etiqueta = tk.Label(ventana, text="Seleccione una figura:")
        self.etiqueta.grid(row=0, column=0, columnspan=2, pady=10)

        self.boton_cilindro = tk.Button(ventana, text="Cilindro", command=self.abrir_ventana_cilindro)
        self.boton_cilindro.grid(row=1, column=0, pady=10)

        self.boton_esfera = tk.Button(ventana, text="Esfera", command=self.abrir_ventana_esfera)
        self.boton_esfera.grid(row=1, column=1, pady=10)

        self.boton_piramide = tk.Button(ventana, text="Pirámide", command=self.abrir_ventana_piramide)
        self.boton_piramide.grid(row=1, column=2, pady=10)

        self.espacio_vacio = tk.Label(ventana, text="")
        self.espacio_vacio.grid(row=2, column=0, columnspan=3)

    def abrir_ventana_cilindro(self):
        ventana_cilindro = tk.Toplevel(self.ventana)
        ventana_cilindro.title("Cálculo de Cilindro")
        ventana_cilindro.geometry("300x200")

        etiqueta_radio = tk.Label(ventana_cilindro, text="Radio (cms):")
        etiqueta_radio.pack()

        campo_radio = tk.Entry(ventana_cilindro)
        campo_radio.pack()

        etiqueta_altura = tk.Label(ventana_cilindro, text="Altura (cms):")
        etiqueta_altura.pack()

        campo_altura = tk.Entry(ventana_cilindro)
        campo_altura.pack()

        boton_calcular = tk.Button(ventana_cilindro, text="Calcular", command=lambda: self.calcular_cilindro(ventana_cilindro, float(campo_radio.get()), float(campo_altura.get())))
        boton_calcular.pack()

    def abrir_ventana_esfera(self):
        ventana_esfera = tk.Toplevel(self.ventana)
        ventana_esfera.title("Cálculo de Esfera")
        ventana_esfera.geometry("300x150")

        etiqueta_radio = tk.Label(ventana_esfera, text="Radio (cms):")
        etiqueta_radio.pack()

        campo_radio = tk.Entry(ventana_esfera)
        campo_radio.pack()

        boton_calcular = tk.Button(ventana_esfera, text="Calcular", command=lambda: self.calcular_esfera(ventana_esfera, float(campo_radio.get())))
        boton_calcular.pack()

    def abrir_ventana_piramide(self):
        ventana_piramide = tk.Toplevel(self.ventana)
        ventana_piramide.title("Cálculo de Pirámide")
        ventana_piramide.geometry("300x200")

        etiqueta_base = tk.Label(ventana_piramide, text="Base (cms):")
        etiqueta_base.pack()

        campo_base = tk.Entry(ventana_piramide)
        campo_base.pack()

        etiqueta_altura = tk.Label(ventana_piramide, text="Altura (cms):")
        etiqueta_altura.pack()

        campo_altura = tk.Entry(ventana_piramide)
        campo_altura.pack()

        etiqueta_apotema = tk.Label(ventana_piramide, text="Apotema (cms):")
        etiqueta_apotema.pack()

        campo_apotema = tk.Entry(ventana_piramide)
        campo_apotema.pack()

        boton_calcular = tk.Button(ventana_piramide, text="Calcular", command=lambda: self.calcular_piramide(ventana_piramide, float(campo_base.get()), float(campo_altura.get()), float(campo_apotema.get())))
        boton_calcular.pack()

    def calcular_cilindro(self, ventana, radio, altura):
        volumen = math.pi * radio**2 * altura
        superficie = 2 * math.pi * radio * (radio + altura)

        self.mostrar_resultados(ventana, volumen, superficie)

    def calcular_esfera(self, ventana, radio):
        volumen = (4/3) * math.pi * radio**3
        superficie = 4 * math.pi * radio**2

        self.mostrar_resultados(ventana, volumen, superficie)

    def calcular_piramide(self, ventana, base, altura, apotema):
        volumen = (1/3) * base * altura
        superficie = base + (1/2) * apotema * base

        self.mostrar_resultados(ventana, volumen, superficie)

    def mostrar_resultados(self, ventana, volumen, superficie):
        etiqueta_volumen = tk.Label(ventana, text=f"Volumen (cms³): {volumen:.2f}")
        etiqueta_volumen.pack()

        etiqueta_superficie = tk.Label(ventana, text=f"Superficie (cms²): {superficie:.2f}")
        etiqueta_superficie.pack()


ventana_principal = tk.Tk()
ventana_principal.title("Cálculo de Figuras Geométricas")
ventana_principal.geometry("300x250")

ventana_figuras = VentanaPrincipal(ventana_principal)

for i in range(3):
    ventana_principal.grid_columnconfigure(i, weight=1)

ventana_principal.mainloop()
