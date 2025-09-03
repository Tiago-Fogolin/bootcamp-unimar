import customtkinter as ctk



def criar_sidebar(janela, tela_cadastro, tela_lista, atualizar_lista):
    def mostrar_tela_cadastro():
        tela_lista.place_forget()
        tela_cadastro.place(x=0, y=0)

    def mostrar_lista_contatos():
        tela_cadastro.place_forget()
        atualizar_lista()
        tela_lista.place(x=0, y=0)


    sidebar = ctk.CTkFrame(janela, width=120, height=720, fg_color="white", bg_color="black")

    botao_tela_cadastro = ctk.CTkButton(sidebar, text="Cadastro", width=100, command=mostrar_tela_cadastro)
    botao_tela_cadastro.place(x=15, y=40)

    botao_lista_cadastro = ctk.CTkButton(sidebar, text="Lista", width=100, command=mostrar_lista_contatos)
    botao_lista_cadastro.place(x=15, y=100)

    return sidebar
