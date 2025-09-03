import customtkinter as ctk
from tela_cadastro import criar_tela_cadastro
from tela_lista_contatos import criar_tela_lista_contatos
from sidebar import criar_sidebar
from sanduiche import criar_sanduiche

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

lista_contatos = []

janela = ctk.CTk()
janela.geometry("800x600")
janela.resizable(False , False)

tela_cadastro = criar_tela_cadastro(janela, lista_contatos)
tela_cadastro.place(x=0,y=0)

tela_lista_contatos, atualizar_lista = criar_tela_lista_contatos(janela, lista_contatos)

sidebar = criar_sidebar(janela, tela_cadastro, tela_lista_contatos, atualizar_lista)

sanduiche = criar_sanduiche(janela, sidebar)
sanduiche.place(x=5,y=0)

janela.mainloop()