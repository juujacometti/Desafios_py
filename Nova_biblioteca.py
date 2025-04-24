import tkinter as tk
import tkinter as ttk

# Lista para armazenar as tarefas
tarefas = []

# Janela principal
janela = tk.Tk()
janela.title("Lista de tarefas")

# Frame principal
frm = ttk.Frame(janela, pady = 20)
frm.grid()

# Label
entrar = (ttk.Label(frm, text="Voce deseja entrar nas suas tarefas?"))
entrar.grid(column=0, row=0)

# Funções para os botões
def clique_sim(adicionar_tarefa=None):
    entrar.grid_forget() # Comando usado para o label anterior desaparecer
    iniciar = (ttk.Label(frm, text="Bem-vindo(a) a sua lista de tarefas!"))
    iniciar.grid(column=0, row=0)

    def adicionar_tarefa():
        nova_tarefa = tk.simpledialog.asktring("Nova tarefa", "Digite a tarefa:")


    botao_adicionar_tarefa = ttk.Button(frm, text="Adicionar nova tarefa", command=adicionar_tarefa)
    botao_adicionar_tarefa.grid(column=0, row=1)

botao_sim = ttk.Button(frm, text="Sim", command=clique_sim)
botao_sim.grid(column=0, row=1, padx=10)

# Encerra o programa
botao_nao = ttk.Button(frm, text="Não", command=janela.destroy)
botao_nao.grid(column=1, row=1, padx=10)

janela.mainloop()