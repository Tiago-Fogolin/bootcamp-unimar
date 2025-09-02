import customtkinter as ctk


janela = ctk.CTk()
janela.geometry("800x600")
janela.title("Titulo da Janela")


label = ctk.CTkLabel(janela, width=200, height=50, text="Primeiro Texto", font=("Arial", 20), text_color="red")
label.place(x=300, y=10)

entrada = ctk.CTkEntry(
                        janela, 
                        width=200, 
                        height=20, 
                        placeholder_text="Escreva seu nome", 
                        font=("Arial", 14)
                    )
entrada.place(x=300, y=100)


def mostrar_nome():
    nome = entrada.get()

    label_nome.configure(text=f"Olá, {nome}!")
    label_nome.place(x=300, y=300)

    print(nome)

botao = ctk.CTkButton(janela, width=100, height=50, text="Me clica", command=mostrar_nome)
botao.place(x=350, y=200)

label_nome = ctk.CTkLabel(janela, width=200, height=50, font=("Arial", 20))

janela.mainloop()
