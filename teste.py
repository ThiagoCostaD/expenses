import tkinter as tk
from tkinter import messagebox


class IMCApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculo IMC")
        self.root.geometry("310x360")
        self.root.resizable(False, False)
        self.root.config(bg="#FF9999")

        self.create_widgets()

    def create_widgets(self):
        # Labels
        self.create_label("Qual o seu peso? (kg)", 85, 30)
        self.create_label("Qual sua altura em centímetros?", 55, 80)
        self.create_label("Resultado:", 117, 130)
        self.create_label("Classificação:", 108, 180)

        # Entry fields
        self.entry_peso = self.create_entry(71, 60)
        self.entry_altura = self.create_entry(71, 110)

        # Result fields
        self.resultado_imc = tk.StringVar()
        self.classificacao = tk.StringVar()

        self.entry_resultado = self.create_entry(
            71, 160, state='readonly', textvariable=self.resultado_imc)
        self.entry_classificacao = self.create_entry(
            71, 210, state='readonly', textvariable=self.classificacao)

        # Button
        self.create_button("Calcular", 97, 260, self.calcular_imc)

    def create_label(self, text, x, y):
        label = tk.Label(self.root, text=text)
        label.place(x=x, y=y)
        label.config(foreground="black", font=("Serif", 13, "bold"))

    def create_entry(self, x, y, **kwargs):
        entry = tk.Entry(self.root, justify='center', **kwargs)
        entry.place(x=x, y=y, width=150)
        return entry

    def create_button(self, text, x, y, command):
        button = tk.Button(self.root, text=text, command=command)
        button.place(x=x, y=y, width=100, height=25)
        button.config(background="white", foreground="black")

    def calcular_imc(self):
        try:
            self._extracted_from_calcular_imc_3()
        except ValueError:
            messagebox.showerror(
                "Erro", "Por favor, insira valores válidos para peso e altura")
            self.resultado_imc.set("")
            self.classificacao.set("")

    # TODO Rename this here and in `calcular_imc`
    def _extracted_from_calcular_imc_3(self):
        peso = float(self.entry_peso.get())
        altura_cm = float(self.entry_altura.get())
        altura_m = altura_cm / 100
        imc = peso / (altura_m ** 2)

        self.resultado_imc.set(f"{imc:.2f}")

        if imc < 17:
            self.classificacao.set("Muito abaixo do peso")
        elif 17 <= imc <= 18.49:
            self.classificacao.set("Abaixo do peso")
        elif 18.5 <= imc <= 24.99:
            self.classificacao.set("Peso normal")
        elif 25 <= imc <= 29.99:
            self.classificacao.set("Acima do peso")
        elif 30 <= imc <= 34.99:
            self.classificacao.set("Obesidade I")
        elif 35 <= imc <= 39.99:
            self.classificacao.set("Obesidade II (severa)")
        else:
            self.classificacao.set("Obesidade III (mórbida)")


if __name__ == "__main__":
    root = tk.Tk()
    app = IMCApp(root)
    root.mainloop()
