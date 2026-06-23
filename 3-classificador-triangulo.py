import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# =============== Tela ===============
janela = tk.Tk()
janela.title("Classificação de triângulos")
janela.geometry("500x500")
janela.resizable(False, False)

janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)

# =============== Funcionamento ===============
def classificaTriangulo():
    try:
        ladoA = float(entrada_lado_a.get())
        ladoB = float(entrada_lado_b.get())
        ladoC = float(entrada_lado_c.get())
        # Verifica nulidade
        if(ladoA <= 0 or ladoB <= 0 or ladoC <= 0):
            messagebox.showerror(title="Erro", message="Insira valores VÁLIDOS!")
            limpaTela()
            return
        classificacao = ""
        cor = ""
    except ValueError:
        # Valor incorreto
        messagebox.showerror(title="Erro", message="O valor deve ser um NÚMERO VÁLIDO!")
        limpaTela()
        return
    
    if not (ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA):
        classificacao = "Não é triângulo"
        cor = "red"
    else:        
        if(ladoA == ladoB == ladoC):
            classificacao = "Equilátero"
            cor = "green"
        elif(ladoA == ladoB != ladoC or ladoA == ladoC != ladoB or ladoB == ladoC != ladoA):
            classificacao = "Isósceles"
            cor = "blue"
        else:
            classificacao = "Escaleno"
            cor = "purple"
    
    label_classificacao.config(text=f"Classificação: {classificacao}", fg=cor)
    return

def limpaTela():
    entrada_lado_a.delete(0, tk.END)
    entrada_lado_b.delete(0, tk.END)
    entrada_lado_c.delete(0, tk.END)
    label_classificacao.config(text="Classificação: N/A", fg="black")
    entrada_lado_a.focus()
    return

# =============== Componentes ===============
label_principal = tk.Label(janela, text="Classificação de triângulos", font=("Sans-serif", 12, "bold"))

label_lado_a = tk.Label(janela, text="Informe o valor do primeiro lado:")
entrada_lado_a = tk.Entry(janela)

label_lado_b = tk.Label(janela, text="Informe o valor do segundo lado:")
entrada_lado_b = tk.Entry(janela)

label_lado_c = tk.Label(janela, text="Informe o valor do terceiro lado:")
entrada_lado_c = tk.Entry(janela)

botao_classifica = tk.Button(janela, text="Classificar", command=classificaTriangulo)
botao_limpar = tk.Button(janela, text="Limpar", command=limpaTela)

label_classificacao = tk.Label(janela, text="Classificação: N/A", font=("Sans-serif", 12, "bold"))

label_principal.grid(row=0, column=0, columnspan=2, sticky="ew", pady=30)
label_lado_a.grid(row=1,column=0, columnspan=2)
entrada_lado_a.grid(row=2,column=0, columnspan=2)
label_lado_b.grid(row=3,column=0, columnspan=2)
entrada_lado_b.grid(row=4,column=0, columnspan=2)
label_lado_c.grid(row=5,column=0, columnspan=2)
entrada_lado_c.grid(row=6,column=0, columnspan=2)
botao_classifica.grid(row=7, column=0, columnspan=2,pady=(30,10))
botao_limpar.grid(row=8, column=0, columnspan=2)
label_classificacao.grid(row=9, column=0, sticky="e", pady=60)

janela.mainloop()