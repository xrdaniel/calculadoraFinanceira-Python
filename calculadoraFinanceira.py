import tkinter as tk
from tkinter import ttk
import math

def calcular_juros_simples():
    principal = float(principal_entry.get())
    taxa = float(taxa_entry.get())
    tempo = float(tempo_entry.get())

    juros = (principal * taxa * tempo) / 100
    resultado_label.config(text=f"Juros Simples: R$ {juros:.2f}")

def calcular_juros_compostos():
    principal = float(principal_entry.get())
    taxa = float(taxa_entry.get())
    tempo = float(tempo_entry.get())

    montante = principal * (1 + taxa / 100) ** tempo
    juros = montante - principal
    resultado_label.config(text=f"Montante: R$ {montante:.2f}\nJuros Compostos: R$ {juros:.2f}")

def calcular_amortizacao():
    principal = float(principal_entry.get())
    taxa = float(taxa_entry.get())
    parcelas = int(parcelas_entry.get())

    amortizacao = principal / parcelas
    juros_total = 0

    for _ in range(parcelas):
        juros = principal * (taxa / 100)
        principal -= amortizacao
        juros_total += juros

    resultado_label.config(text=f"Amortização por parcela: R$ {amortizacao:.2f}\nTotal de Juros: R$ {juros_total:.2f}")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Calculadora Financeira")

principal_label = ttk.Label(root, text="Principal:")
principal_label.pack()

principal_entry = ttk.Entry(root)
principal_entry.pack()

taxa_label = ttk.Label(root, text="Taxa de Juros (%):")
taxa_label.pack()

taxa_entry = ttk.Entry(root)
taxa_entry.pack()

tempo_label = ttk.Label(root, text="Tempo (anos):")
tempo_label.pack()

tempo_entry = ttk.Entry(root)
tempo_entry.pack()

calcular_juros_simples_button = ttk.Button(root, text="Calcular Juros Simples", command=calcular_juros_simples)
calcular_juros_simples_button.pack()

calcular_juros_compostos_button = ttk.Button(root, text="Calcular Juros Compostos", command=calcular_juros_compostos)
calcular_juros_compostos_button.pack()

parcelas_label = ttk.Label(root, text="Número de Parcelas:")
parcelas_label.pack()

parcelas_entry = ttk.Entry(root)
parcelas_entry.pack()

calcular_amortizacao_button = ttk.Button(root, text="Calcular Amortização", command=calcular_amortizacao)
calcular_amortizacao_button.pack()

resultado_label = ttk.Label(root, text="")
resultado_label.pack()

root.mainloop()
