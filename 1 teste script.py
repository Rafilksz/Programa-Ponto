import mysql.connector
from tkinter import *
from tkinter import messagebox
from funcoes import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def buscar_nomes_funcionarios():
    try:
        con = mysql.connector.connect(host='localhost', database='db_ponto', user='root', password='D@t@W@y.1419')
        consulta_sql = 'SELECT nome FROM tbl_funcionarios'
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        nomes = [linha[0] for linha in linhas]  # Extrai os nomes da lista de tuplas

        return nomes
    except Error as e:
        print(f"Erro ao buscar nomes dos funcionários: {e}")
    finally:
        if con.is_connected():
            cursor.close()
            con.close()




def close():
    janela_mudanca.destroy()
    admwindows()
    con.close()
    cursor.close()
    print('conexao mysql fechada')


def salvar():
    # Obter os valores selecionados
    nome_funcionario = nomes_fun.get()
    data_selecionada = data_new.get()
    hora_selecionada = hora_new.get()
    horario_selecionado = cb_horario.get()

    # Converter o formato da data de DD-MM-YYYY para YYYY-MM-DD
    data_formatada = datetime.datetime.strptime(data_selecionada, '%d-%m-%Y').strftime('%Y-%m-%d')

    # Resto do código permanece o mesmo...


    # Mapear os valores de cb_horario para as colunas correspondentes
    colunas_horario = {
        'Inicio Expediente': 'ini_exp_time',
        'Inicio Almoço': 'ini_alm_time',
        'Fim Almoço': 'fim_alm_time',
        'Fim Expediente': 'fim_exp_time'
    }

    coluna_horario = colunas_horario.get(horario_selecionado, '')

    if nome_funcionario and data_formatada and coluna_horario:
        try:
            con = mysql.connector.connect(host='localhost', database='db_ponto', user='root', password='D@t@W@y.1419')
            cursor = con.cursor()

            # Verificar se já existe um registro com os mesmos valores de nome_funcionario e data
            select_sql = "SELECT * FROM tbl_horario WHERE nomefuncionario = %s AND data = %s"
            cursor.execute(select_sql, (nome_funcionario, data_formatada))
            resultado = cursor.fetchone()

            if resultado:
                # Se o registro já existe, atualize a coluna correspondente
                update_sql = f"UPDATE tbl_horario SET {coluna_horario} = %s WHERE nomefuncionario = %s AND data = %s"
                cursor.execute(update_sql, (hora_selecionada, nome_funcionario, data_formatada))
            else:
                # Se o registro não existe, insira um novo registro com os valores adequados
                insert_sql = "INSERT INTO tbl_horario (nomefuncionario, data, " + coluna_horario + ") VALUES (%s, %s, %s)"
                cursor.execute(insert_sql, (nome_funcionario, data_formatada, hora_selecionada))

            con.commit()
            messagebox.showinfo("Sucesso", "Registro atualizado com sucesso!")

        except mysql.connector.Error as e:
            messagebox.showerror("Erro", f"Erro ao atualizar registro: {e}")
        finally:
            if con.is_connected():
                cursor.close()
                con.close()
    else:
        messagebox.showerror("Erro", "Por favor, selecione um funcionário, data, hora e horário válidos.")


# Resto do seu código...




def formatar_data(event):
    data = data_new.get()
    if len(data) == 2:
        data_new.delete(0, END)
        data_new.insert(0, data + '-')
    elif len(data) == 5:
        data_new.delete(0, END)
        data_new.insert(0, data + '-')
    elif len(data) == 10:
        hora_new.focus_set()  # Set focus to hora_new field


# Função para formatar a entrada de hora no estilo HH:MM
def formatar_hora(event):
    hora = hora_new.get()

    # Remova qualquer caractere que não seja um dígito
    hora = ''.join(filter(str.isdigit, hora))

    if len(hora) == 2:
        hora_new.delete(0, END)
        hora_new.insert(0, hora + ':')
    elif len(hora) == 4:
        hora_new.delete(0, END)
        hora_new.insert(0, hora[:2] + ':' + hora[2:] + ':00')
        cb_horario.focus_set()  # Definir o foco para cb_horario
    elif len(hora) == 8:
        hora_new.delete(0, END)
        hora_new.insert(0, hora[:5] + ':00')
        cb_horario.focus_set()  # Definir o foco para cb_horario


janela_mudanca = customtkinter.CTk()
janela_mudanca.title("Controle de Ponto Dataway")
janela_mudanca.geometry("260x160")
janela_mudanca.resizable(width=False, height=False)
center(janela_mudanca)


listhr = ['Inicio Expediente','Inicio Almoço','Fim Almoço','Fim Expediente']


nomes_funcionarios = buscar_nomes_funcionarios()  # Obtém os nomes dos funcionários do banco de dados
nomes_fun = customtkinter.CTkComboBox(master=janela_mudanca, values=nomes_funcionarios, width=250)
nomes_fun.set("Selecione o Funcionário")
nomes_fun.grid(row=0, column=0, padx=5, pady=5, )

data_new = customtkinter.CTkEntry(janela_mudanca, placeholder_text="DD/MM/AAAA", width=100, height=30, )
data_new.grid(row=1, column=0, padx=5, pady=5, sticky="w")
data_new.bind('<KeyRelease>', formatar_data)

hora_new = customtkinter.CTkEntry(janela_mudanca, placeholder_text="HH:MM", width=60, height=30, )
hora_new.grid(row=1, column=0, padx=5, pady=5, sticky="e")


data_new.bind('<KeyRelease>', formatar_data)
hora_new.bind('<KeyRelease>', formatar_hora)


cb_horario = customtkinter.CTkComboBox(janela_mudanca, values=listhr, width=250)
(cb_horario.set("Horario esquecido"))
cb_horario.grid(row=2, column=0, padx=5, pady=5, )

botao_voltar = customtkinter.CTkButton(
    janela_mudanca, text="Voltar", command=close,
    width=30, height=30, border_width=2, )
botao_voltar.grid(row=3, column=0, padx=5, pady=5, sticky="e")

botao_salvar = customtkinter.CTkButton(
    janela_mudanca, text="Salvar", command=salvar,
    width=30, height=30, border_width=2, )
botao_salvar.grid(row=3, column=0, padx=5, pady=5, )




janela_mudanca.mainloop()
