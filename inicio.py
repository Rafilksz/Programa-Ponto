import customtkinter as tk
import funcoes
import tkinter.messagebox
import mysql.connector
from tkinter import PhotoImage
from PIL import Image, ImageTk
import tkinter as tk2
import janela_c

def center(win):#faz janelas abrirem no meio da tela
    # :param win: the main window or Toplevel window to center
    # Apparently a common hack to get the window size. Temporarily hide the
    # window to avoid update_idletasks() drawing the window in the wrong
    # position.
    win.update_idletasks()  # Update "requested size" from geometry manager
    # define window dimensions width and height
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    # Get the window position from the top dynamically as well as position from left or right as follows
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    # this is the line that will center your window
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    # This seems to draw the window frame immediately, so only call deiconify()
    # after setting correct window position
    win.deiconify()
    # usar codigo center(NOME DA JANELA) para chamar função     #

# Função para verificar as credenciais e determinar o tipo de usuário

def verificar_credenciais(usuario, senha):
    try:
        con = mysql.connector.connect(host="localhost", database="db_ponto", user="root", password="D@t@W@y.1419")
        cursor = con.cursor()

        query = "SELECT adm, nome FROM tbl_funcionarios WHERE id_funcionario = %s AND senha = %s"
        cursor.execute(query, (usuario, senha))
        resultado = cursor.fetchone()

        if resultado:
            adm = resultado[0]
            nome_usuario = resultado[1]
            id_funcionario =usuario
            if adm == 1:
                janela_login.destroy()
                funcoes.admwindows()  # Passe o nome do usuário para a função admwindows
            elif adm == 0:
                janela_login.destroy()
                janela_c.clientewindows(nome_usuario,id_funcionario)  # Passe o nome do usuário para a função clientewindows
            else:
                userdesc = tk.CTk()
                userdesc.title("Erro")
                tk.set_appearance_mode("dark")
                tk.set_default_color_theme("dark-blue")
                userdesc.geometry("300x100")
                userdesc.configure(bg_color="#FF0000")  # Define a cor de fundo para vermelho

                erro_label2 = tk.CTkLabel(userdesc, text="Tipo de usuário desconhecido")
                erro_label2.pack(padx=10, pady=10)

                fechar_botao = tk.CTkButton(userdesc, text="Fechar", command=userinvalido.destroy)
                fechar_botao.pack(padx=10, pady=10)

                userdesc.mainloop()
        else:
            tkinter.messagebox.showerror("Erro", "Credenciais inválidas")


    except mysql.connector.Error as e:
        print("Erro ao conectar ao banco de dados:", e)
    finally:
        cursor.close()
        con.close()

def mostrar_erro():
    erro_janela = tk.CTk()
    erro_janela.title("Erro")
    tk.set_appearance_mode("dark")
    tk.set_default_color_theme("dark-blue")
    erro_janela.geometry("300x100")
    erro_janela.configure(bg_color="#FF0000")  # Define a cor de fundo para vermelho

    erro_label = tk.CTkLabel(erro_janela, text="Por favor, preencha todos os campos.")
    erro_label.pack(padx=10, pady=10)

    fechar_botao = tk.CTkButton(erro_janela, text="Fechar", command=erro_janela.destroy)
    fechar_botao.pack(padx=10, pady=10)

    erro_janela.mainloop()

def login_ok():
    usuario = user_id.get()
    senha = password_id.get()

    if not usuario or not senha:
        mostrar_erro()
        return

    verificar_credenciais(usuario, senha)


# Configure o tema "dark-blue" para o customtkinter
tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")

janela_login = tk.CTk()
janela_login.title("Controle de Ponto Dataway")
janela_login.geometry("300x400")
janela_login.resizable(width=False, height=False)
center(janela_login)
image_path = "C:\\programa ponto\\img\\User_login.png"

def open_image(file_path):
    image = Image.open(file_path)
    photo = ImageTk.PhotoImage(image)
    label = tk2.Label(janela_login, image=photo,width=150, height=150,anchor="center",background="#191919",)
    label.image = photo  # Mantém uma referência para a imagem
    label.grid(row=0, column=0, padx=5, pady=5, columnspan=300,)

# Chame a função para exibir a imagem
open_image(image_path)



texto = tk.CTkLabel(janela_login, text="Faça o Login",width=300, height=30,font=("arial", 20))
texto.grid(row=1, column=0, padx=5, pady=10, columnspan=300,)

user_id = tk.CTkEntry(janela_login, placeholder_text="CPF somente números",width=250, height=30)
user_id.grid(row=2, column=0, padx=5, pady=10, columnspan=300,)

password_id = tk.CTkEntry(janela_login, placeholder_text="Sua senha", show="*",width=250, height=30)
password_id.grid(row=3, column=0, padx=5, pady=15, columnspan=300,)

botao_login = tk.CTkButton(janela_login, text="Entrar", command=login_ok,width=100, height=30)
botao_login.grid(row=5, column=0, padx=5, pady=15, columnspan=300,)

janela_login.mainloop()