import customtkinter as ctk


def criar_sanduiche(janela, sidebar):
    sidebar_aberta = ctk.BooleanVar(value=False)

    def controla_sidebar():

        if not sidebar_aberta.get():
            sidebar.place(x=5,y=0)
        else:
            sidebar.place_forget()

        sidebar_aberta.set(not sidebar_aberta.get())
        

    sanduiche = ctk.CTkButton(janela, text="☰", width=10, command=controla_sidebar)
    return sanduiche