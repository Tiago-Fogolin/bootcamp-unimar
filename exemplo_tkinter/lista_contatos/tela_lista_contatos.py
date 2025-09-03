import customtkinter as ctk


def criar_tela_lista_contatos(janela, lista_contatos):
    tela_contatos = ctk.CTkFrame(janela, width=800, height=600)

    label_contatos = ctk.CTkLabel(tela_contatos, text="Lista de Contatos", font=("Arial", 14))
    label_contatos.place(x=400, y=10)

    quadro_contatos = ctk.CTkScrollableFrame(tela_contatos, width=400, height=400)
    quadro_contatos.place(x=300, y=150)

    quadro_contatos.grid_columnconfigure(0, weight=1)
    quadro_contatos.grid_columnconfigure(1, weight=1)  

    
    def atualizar_lista():
        linha_atual = 1
        for widget in quadro_contatos.winfo_children(): 
            widget.destroy()

        label_nome = ctk.CTkLabel(quadro_contatos, text="Nome", font=("Arial", 10), text_color="white")
        label_nome.grid(row=0,column=0, padx=20, pady=15, sticky="w")

        label_celular = ctk.CTkLabel(quadro_contatos, text="Celular", font=("Arial", 10), text_color="white")
        label_celular.grid(row=0, column=1, padx=100, pady=15, sticky="e")

        
        for nome, celular in lista_contatos:
            label_nome = ctk.CTkLabel(quadro_contatos, text=nome, font=("Arial", 10))
            label_nome.grid(row=linha_atual, column=0, padx=20, pady=15, sticky="w")

            label_celular = ctk.CTkLabel(quadro_contatos, text=celular, font=("Arial", 10))
            label_celular.grid(row=linha_atual, column=1, padx=100, pady=15, sticky="e")
        
            linha_atual += 1

    atualizar_lista()

    return tela_contatos, atualizar_lista

