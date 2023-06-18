import tkinter as tk
import statistics

class VentanaNotas:
    def __init__(self, ventana):
        self.ventana = ventana
        self.notas = []

        self.etiqueta = tk.Label(ventana, text="Ingrese las notas:")
        self.etiqueta.pack()

        self.campos_notas = []
        for i in range(5):
            frame = tk.Frame(ventana)
            frame.pack()

            etiqueta_nota = tk.Label(frame, text=f"Nota {i+1}:")
            etiqueta_nota.pack(side=tk.LEFT)

            campo_nota = tk.Entry(frame)
            campo_nota.pack(side=tk.LEFT)

            self.campos_notas.append(campo_nota)

        tk.Label(ventana).pack()

        frame_botones = tk.Frame(ventana)
        frame_botones.pack()

        self.boton_calcular = tk.Button(frame_botones, text="Calcular", command=self.calcular)
        self.boton_calcular.pack(side=tk.LEFT, padx=5)

        self.boton_limpiar = tk.Button(frame_botones, text="Limpiar", command=self.limpiar)
        self.boton_limpiar.pack(side=tk.LEFT, padx=5)

        tk.Label(ventana).pack()

        self.etiqueta_promedio = tk.Label(ventana)
        self.etiqueta_promedio.pack()

        self.etiqueta_desviacion = tk.Label(ventana)
        self.etiqueta_desviacion.pack()

        self.etiqueta_mayor = tk.Label(ventana)
        self.etiqueta_mayor.pack()

        self.etiqueta_menor = tk.Label(ventana)
        self.etiqueta_menor.pack()

    def calcular(self):
        self.notas = [float(campo.get()) for campo in self.campos_notas]

        promedio = sum(self.notas) / len(self.notas)
        self.etiqueta_promedio.config(text=f"Promedio: {promedio:.2f}")

        desviacion = statistics.stdev(self.notas) if len(self.notas) > 1 else 0
        self.etiqueta_desviacion.config(text=f"Desviación estándar: {desviacion:.3f}")

        mayor = max(self.notas)
        menor = min(self.notas)
        self.etiqueta_mayor.config(text=f"Mayor nota: {mayor}")
        self.etiqueta_menor.config(text=f"Menor nota: {menor}")

    def limpiar(self):
        for campo in self.campos_notas:
            campo.delete(0, tk.END)
        self.etiqueta_promedio.config(text="")
        self.etiqueta_desviacion.config(text="")
        self.etiqueta_mayor.config(text="")
        self.etiqueta_menor.config(text="")


ventana_principal = tk.Tk()
ventana_principal.title("Cálculo de Notas")
ventana_principal.geometry("300x300")

ventana_notas = VentanaNotas(ventana_principal)

ventana_principal.mainloop()
