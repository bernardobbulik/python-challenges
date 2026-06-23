import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# =============== Tela ===============
janela = tk.Tk()
janela.title("Desempenho do desempenho")
janela.geometry("500x500")
janela.resizable(False, False)

janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)

# =============== Funcionamento ==============
def verificaDesempenho():
    # Entrada e Processamento
    try:
        vitorias = int(entrada_vitorias.get())
        empates = int(entrada_empates.get())
        derrotas = int(entrada_derrotas.get())
    except ValueError:
        messagebox.showerror(title="Erro", message="Insira somente VALORES VÁLIDOS!")
        limpaTela()
        return
    
    if(vitorias < 0 or empates < 0 or derrotas < 0):
        messagebox.showerror(title="Erro", message="Insira valores POSITIVOS!")
        limpaTela()
        return
    
    try:
        classificacao = ""
        cor = ""
        totalPontos = (vitorias * 3) + (empates * 1)
        maximoPontos = (vitorias + empates + derrotas) * 3
        aproveitamento = (totalPontos / maximoPontos) * 100
        
        if(aproveitamento >= 70):
            classificacao = "EXCELENTE"
            cor = "green"
        elif(aproveitamento >= 50 and aproveitamento < 70):
            classificacao = "BOM"
            cor = "orange"
        elif(aproveitamento >= 30 and aproveitamento < 50):
            classificacao = "REGULAR"
            cor = "yellow"
        else:
            classificacao = "RUIM"
            cor = "red"
    except ArithmeticError:
        messagebox.showerror(title="Erro",message="Houve um erro ao calcular o desempenho.")
        limpaTela()
        return
    
    
    # Saída
    label_aproveitamento.config(text=f"Aproveitamento: {aproveitamento:.2f}%")
    label_pontos.config(text=f"Pontos: {totalPontos}")
    label_classificacao.config(text=f"Classificação: {classificacao}", fg=cor)
    return
    
def limpaTela():
    cor = "black"
    label_aproveitamento.config(text=f"Aproveitamento: N/A", fg=cor)
    label_pontos.config(text=f"Pontos: N/A", fg=cor)
    label_classificacao.config(text=f"Classificação: N/A", fg=cor)
    
    entrada_derrotas.delete(0, tk.END)
    entrada_vitorias.delete(0, tk.END)
    entrada_empates.delete(0, tk.END)
    
    entrada_vitorias.focus()
    
    return

# =============== Componentes ===============
label_principal = tk.Label(janela, text="Classificação de desempenho", font=("Sans-serif", 12, "bold"))

label_vitorias = tk.Label(janela, text="Quantidade de vitórias:")
entrada_vitorias = tk.Entry(janela)

label_empates = tk.Label(janela, text="Quantidade de empates:")
entrada_empates = tk.Entry(janela)

label_derrotas = tk.Label(janela, text="Quantidade de derrotas:")
entrada_derrotas = tk.Entry(janela)

botao_classifica = tk.Button(janela, text="Classificar", command=verificaDesempenho)
botao_limpar = tk.Button(janela, text="Limpar", command=limpaTela)

label_pontos = tk.Label(janela, text="Pontos: N/A", font=("Sans-serif", 12, "bold"))
label_aproveitamento = tk.Label(janela, text="Aproveitamento: N/A", font=("Sans-serif", 12, "bold"))
label_classificacao = tk.Label(janela, text="Classificação: N/A", font=("Sans-serif", 12, "bold"))

label_principal.grid(row=0, column=0, columnspan=2, sticky="ew", pady=30)

label_vitorias.grid(row=1,column=0, columnspan=2)
entrada_vitorias.grid(row=2,column=0, columnspan=2)

label_empates.grid(row=3,column=0, columnspan=2)
entrada_empates.grid(row=4,column=0, columnspan=2)

label_derrotas.grid(row=5,column=0, columnspan=2)
entrada_derrotas.grid(row=6,column=0, columnspan=2)

botao_classifica.grid(row=7, column=0, columnspan=2,pady=(30,10))
botao_limpar.grid(row=8, column=0, columnspan=2)

label_pontos.grid(row=9, column=0, columnspan=2, pady=(30,0))
label_aproveitamento.grid(row=10, column=0, columnspan=2)
label_classificacao.grid(row=11, column=0, columnspan=2)

janela.mainloop()