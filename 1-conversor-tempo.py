import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# =============== Tela ===============
janela = tk.Tk()
janela.title("Conversor de Tempo")
janela.geometry("350x270")
janela.resizable(False, False)

# =============== Funcionamento ===============
def converteSegundos():
    try:
        totalSegundos = int(entrada_segundos.get())
    except ValueError:
        messagebox.showerror(title='Erro', message='Entrada deve ser um número válido!')
        cleanScreen()
        return
    if(totalSegundos <= 0):
        messagebox.showwarning(title='Aviso', message='Entrada não pode ser vazia ou negativa!')
        return
    horas = totalSegundos // 3600
    minutos = (totalSegundos % 3600) // 60
    segundos = totalSegundos % 60
    
    label_horas.config(text=f"Horas: {horas}")
    label_minutos.config(text=f"Minutos: {minutos}")
    label_segundos.config(text=f"Segundos: {segundos}")
        

def cleanScreen():
    label_minutos.config(text="Minutos: 0")
    label_horas.config(text="Horas: 0")
    label_segundos.config(text="Segundos: 0")
    entrada_segundos.delete(0, tk.END)

# Título
titulo = ttk.Label(
    janela,
    text="Conversor de Tempo",
    font=("Arial", 11, "bold")
)
titulo.pack(pady=12)

# Área do input
frame_input = ttk.Frame(janela)
frame_input.pack(pady=10)

ttk.Label(frame_input, text="Total de segundos:").grid(row=0, column=0, padx=8)

entrada_segundos = ttk.Entry(frame_input, width=20)
entrada_segundos.grid(row=0, column=1)

# Botões
frame_botoes = ttk.Frame(janela)
frame_botoes.pack(pady=15)

ttk.Button(frame_botoes, text="Converter", command=converteSegundos).grid(row=0, column=0, padx=5)
ttk.Button(frame_botoes, text="Limpar", command=cleanScreen).grid(row=0, column=1, padx=5)
ttk.Button(frame_botoes, text="Sair", command=janela.destroy).grid(row=0, column=2, padx=5)

# Resultado
frame_resultado = ttk.LabelFrame(janela, text="Resultado")
frame_resultado.pack(padx=20, pady=5, fill="x")

label_horas = ttk.Label(frame_resultado, text="Horas: 0")
label_horas.pack(anchor="w", padx=10, pady=3)

label_minutos = ttk.Label(frame_resultado, text="Minutos: 0")
label_minutos.pack(anchor="w", padx=10, pady=3)

label_segundos = ttk.Label(frame_resultado, text="Segundos: 0")
label_segundos.pack(anchor="w", padx=10, pady=3)

cleanScreen()

janela.mainloop()