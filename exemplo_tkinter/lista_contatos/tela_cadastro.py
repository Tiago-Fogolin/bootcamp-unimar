import customtkinter as ctk
import tkinter as tk

def criar_tela_cadastro(janela, lista_contatos):
    
    def cadastrar():
        nome_cadastrar = nome_contato.get()
        celular_cadastrar = celular_contato.get()

        nome_contato.delete(0, tk.END)
        celular_contato.delete(0, tk.END)

        lista_contatos.append((nome_cadastrar, celular_cadastrar))


    tela_cadastro = ctk.CTkFrame(janela, width=800, height=600)

    label_cadastro = ctk.CTkLabel(tela_cadastro, text="Cadastro de Contato", font=("Arial", 14))
    label_cadastro.place(x=350, y=10)

    nome_contato = ctk.CTkEntry(tela_cadastro, width=200, height=50, placeholder_text="Nome do contato")
    nome_contato.place(x=350, y=200)

    celular_contato = ctk.CTkEntry(tela_cadastro, width=200, height=50, placeholder_text="Celular do contato")
    celular_contato.place(x=350, y=300)

    botao_cadastrar = ctk.CTkButton(tela_cadastro, width=100, height=50, command=cadastrar, text="Cadastrar")
    botao_cadastrar.place(x=400, y=400)

    return tela_cadastro

