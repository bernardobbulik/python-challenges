import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import math

# =============== Tela ===============
janela = tk.Tk()
janela.title("Verificador de número primo")
janela.geometry("400x200")
janela.resizable(False, False)

janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)

# =============== Funcionamento ==============
def eh_primo(num: int):
    '''
    Debug ->
    num = 16
    raizQuadrada = 4
    4 % 2 = 0 -> não é primo
    
    num = 7
    raizQuadrada = 2.64
    2.64 / 2 == 1 -> é primo
    '''
    if(num <= 1):
        return False

    raizQuadrada = int(math.sqrt(num))
    for i in range(2, raizQuadrada + 1):
        if(num % i) == 0:
            return False
    
    return True
        
def verificaPrimo():
    try:
        num = int(entrada_numero.get())
        
        if(num < 0):
            messagebox.showerror(title="Erro", message="Informe um número MAIOR QUE ZERO!")
            return
        
        if(eh_primo(num)):
            label_resultado.config(text="Resultado: PRIMO", fg="green")
        else:
            label_resultado.config(text="Resultado: NÃO É PRIMO", fg="red")    
        return
    except ValueError:
        messagebox.showerror(title="Erro", message="Informe um NÚMERO VÁLIDO!")
        limpaTela()
        return
    
    
def limpaTela():
    entrada_numero.delete(0, tk.END)
    label_resultado.config(text="Resultado:", fg="black")
    
    entrada_numero.focus()
    return

# =============== Componentes ===============
label_principal = tk.Label(janela, text="Verificador de número primo", font=("Sans-serif", 12, "bold"))

label_numero = tk.Label(janela, text="Informe o número:")
entrada_numero = tk.Entry(janela)

botao_verifica = tk.Button(janela, text="Verificar", command=verificaPrimo)

label_resultado = tk.Label(janela, text="Resultado: N/A", font=("Sans-serif", 12, "bold"))

label_principal.grid(row=0, column=0, columnspan=2,pady=40)
label_numero.grid(row=1, column=0)
entrada_numero.grid(row=2, column=0)
botao_verifica.grid(row=2, column=1, columnspan=2, sticky="we", padx=(0, 30))
label_resultado.grid(row=3, column=0, columnspan=2, pady=(20, 10))
janela.mainloop()