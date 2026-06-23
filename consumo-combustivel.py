import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# =============== Tela ===============
janela = tk.Tk()
janela.title("Consumo de combustível")
janela.geometry("500x500")
janela.resizable(False, False)

janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)

# =============== Funcionamento ===============
def calculaConsumo():
    '''
    Consumo = Distancia / Litros
    >= 14 - excelente
    >= 10 < 14 - bom
    >= 7 < 10 - regular
    < 7 - ruim
    '''
    try:
        distancia = float(entrada_distancia.get())
        consumo = float(entrada_consumo.get())
        classificacao = ""
        cor = ""
    except ValueError:
        messagebox.showerror(title="Erro", message="Os valores não podem ser LETRAS!")
        limpaTela()
        return
    
    if(distancia <= 0 or consumo <= 0):
        messagebox.showerror(title="Erro", message="Os valores devem ser VÁLIDOS e POSITIVOS!")
        limpaTela()
        return
    
    mediaConsumo = distancia / consumo
    
    if(mediaConsumo >= 14):
        classificacao = "Excelente"
        cor = "green"
    elif(mediaConsumo >= 10 and mediaConsumo < 14):
        classificacao = "Bom"
        cor = "orange"
    elif(mediaConsumo >= 7 and mediaConsumo < 10):
        classificacao = "Regular"
        cor = "yellow"
    else:
        classificacao = "Ruim"
        cor = "red"
        
    label_consumoMedio.config(text=f"Consumo: {mediaConsumo:.2f}km/L")
    label_classificacao.config(text=f"Classificação: {classificacao}", fg=cor)
        
    return

def limpaTela():
    entrada_distancia.delete(0, tk.END)
    entrada_consumo.delete(0, tk.END)
    label_consumoMedio.config(text="Consumo: N/A")
    label_classificacao.config(text="Classificação: N/A", fg="black")
    entrada_distancia.focus()
    return

# =============== Componentes ===============
label_principal = tk.Label(janela, text="Eficiência de consumo", font=("Sans-serif", 12, "bold"))

label_distancia = tk.Label(janela, text="Informe a distância percorrida (Km):")
entrada_distancia = tk.Entry(janela)

label_consumo = tk.Label(janela, text="Informe o consumo de combustível (L):")
entrada_consumo = tk.Entry(janela)

botao_calcula = tk.Button(janela, text="Calcular", command=calculaConsumo)
botao_limpar = tk.Button(janela, text="Limpar", command=limpaTela)

label_consumoMedio = tk.Label(janela, text="Consumo: N/A", font=("Sans-serif", 11, "bold"))
label_classificacao = tk.Label(janela, text="Classificação: N/A", font=("Sans-serif", 11, "bold"))

label_principal.grid(row=0, column=0, columnspan=2, sticky="ew", pady=10)
label_distancia.grid(row=1,column=0, columnspan=2, sticky="ew", pady=5)
entrada_distancia.grid(row=2, column=0, columnspan=2)
label_consumo.grid(row=3,column=0, columnspan=2, sticky="ew", pady=5)
entrada_consumo.grid(row=4, column=0, columnspan=2)
botao_calcula.grid(row=5, column=0, pady=30)
botao_limpar.grid(row=5, column=1, pady=30)
label_consumoMedio.grid(row=6, column=0, sticky="e")
label_classificacao.grid(row=7, column=0, sticky="e")

janela.mainloop()