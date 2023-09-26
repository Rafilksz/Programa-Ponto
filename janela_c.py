import mysql.connector
import customtkinter
from funcoes import *
import datetime as dt

def clientewindows(nome_usuario,id_funcionario):

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    janela_ponto = customtkinter.CTk()
    janela_ponto.geometry("560x200")
    janela_ponto.title("Menu de Ponto")
    janela_ponto.resizable(width=False, height=False)
    center(janela_ponto)


    nomedapessoa = customtkinter.CTkLabel(
        janela_ponto,
        width=400,
        height=50,
        text=f"Nome: {nome_usuario} \n ID: {id_funcionario}",
        font=("arial", 30),
        anchor="center",
        corner_radius=2)
    (nomedapessoa.grid(row=0, column=1, padx=5, pady=5, columnspan=560))

    def atualizar_hora():
        agora = dt.datetime.now()
        data_hora_formatada = agora.strftime("%d/%m/%Y    %H:%M:%S")
        label_data_hora.configure(text=data_hora_formatada)  # Use configure em vez de config
        janela_ponto.after(1000, atualizar_hora)

    def inserir_ini_exp():
        try:
            con = mysql.connector.connect(
                host="localhost",
                database="db_ponto",
                user="root",
                password="D@t@W@y.1419"
            )
            cursor = con.cursor()

            # Obtém a data e hora atual
            agora = dt.datetime.now()
            data_atual = agora.strftime("%Y-%m-%d")
            horario_atual = agora.strftime("%H:%M:%S")

            # Insere os dados na tabela
            sql = "INSERT INTO tbl_horario (idfuncionarios, nomefuncionario, data, ini_exp_time) VALUES (%s, %s, %s, %s)"
            val = (id_funcionario, nome_usuario, data_atual, horario_atual)
            cursor.execute(sql, val)

            con.commit()
            con.close()
            messagebox.showinfo("Sucesso", "Horário inserido com sucesso! Bom Trabalho!")

        except Exception as e:
            messagebox.showinfo(f"Erro ao inserir registro: {str(e)}")

    def inserir_ini_alm():
        try:
            con = mysql.connector.connect(
                host="localhost",
                database="db_ponto",
                user="root",
                password="D@t@W@y.1419"
            )
            cursor = con.cursor()

            # Obtém a data e hora atual
            agora = dt.datetime.now()
            data_atual = agora.strftime("%Y-%m-%d")
            horario_atual = agora.strftime("%H:%M:%S")

            # Verifica se já existe um registro com os mesmos valores
            sql_verificacao = "SELECT COUNT(*) FROM tbl_horario WHERE idfuncionarios = %s AND nomefuncionario = %s AND data = %s"
            val_verificacao = (id_funcionario, nome_usuario, data_atual)
            cursor.execute(sql_verificacao, val_verificacao)
            resultado = cursor.fetchone()[0]

            if resultado > 0:
                # Registros encontrados, atualize-os
                sql_atualizacao = "UPDATE tbl_horario SET ini_alm_time = %s WHERE idfuncionarios = %s AND nomefuncionario = %s AND data = %s"
                val_atualizacao = (horario_atual, id_funcionario, nome_usuario, data_atual)
                cursor.execute(sql_atualizacao, val_atualizacao)
                con.commit()
                con.close()
                messagebox.showinfo("Sucesso", "Horário inserido com sucesso! Bom Almoço!")
            else:
                # Nenhum registro encontrado, não faça nada
                messagebox.showinfo("Nenhum registro encontrado. Nenhum registro foi atualizado.")

        except Exception as e:
            messagebox.showinfo(f"Erro ao inserir ou atualizar registro de início do Almoço: {str(e)}")

    def inserir_fim_alm():
        try:
            con = mysql.connector.connect(
                host="localhost",
                database="db_ponto",
                user="root",
                password="D@t@W@y.1419"
            )
            cursor = con.cursor()

            # Obtém a data e hora atual
            agora = dt.datetime.now()
            data_atual = agora.strftime("%Y-%m-%d")
            horario_atual = agora.strftime("%H:%M:%S")

            # Verifica se já existe um registro com os mesmos valores
            sql_verificacao = "SELECT COUNT(*) FROM tbl_horario WHERE idfuncionarios = %s AND nomefuncionario = %s AND data = %s"
            val_verificacao = (id_funcionario, nome_usuario, data_atual)
            cursor.execute(sql_verificacao, val_verificacao)
            resultado = cursor.fetchone()[0]

            if resultado > 0:
                # Registros encontrados, atualize-os
                sql_atualizacao = "UPDATE tbl_horario SET fim_alm_time = %s WHERE idfuncionarios = %s AND nomefuncionario = %s AND data = %s"
                val_atualizacao = (horario_atual, id_funcionario, nome_usuario, data_atual)
                cursor.execute(sql_atualizacao, val_atualizacao)
                con.commit()
                con.close()
                messagebox.showinfo("Sucesso", "Horário inserido com sucesso! Bom Trabalho!")
            else:
                # Nenhum registro encontrado, não faça nada
                messagebox.showinfo("Nenhum registro encontrado. Nenhum registro foi atualizado.")

        except Exception as e:
            messagebox.showinfo(f"Erro ao inserir ou atualizar registro de fim do Almoço: {str(e)}")

    def inserir_fim_exp():
        try:
            con = mysql.connector.connect(
                host="localhost",
                database="db_ponto",
                user="root",
                password="D@t@W@y.1419"
            )
            cursor = con.cursor()

            # Obtém a data e hora atual
            agora = dt.datetime.now()
            data_atual = agora.strftime("%Y-%m-%d")
            horario_atual = agora.strftime("%H:%M:%S")

            # Verifica se já existe um registro com os mesmos valores
            sql_verificacao = "SELECT COUNT(*) FROM tbl_horario WHERE idfuncionarios = %s AND nomefuncionario = %s AND data = %s"
            val_verificacao = (id_funcionario, nome_usuario, data_atual)
            cursor.execute(sql_verificacao, val_verificacao)
            resultado = cursor.fetchone()[0]

            if resultado > 0:
                # Registros encontrados, atualize-os
                sql_atualizacao = "UPDATE tbl_horario SET fim_exp_time = %s WHERE idfuncionarios = %s AND nomefuncionario = %s AND data = %s"
                val_atualizacao = (horario_atual, id_funcionario, nome_usuario, data_atual)
                cursor.execute(sql_atualizacao, val_atualizacao)
                con.commit()
                con.close()
                messagebox.showinfo("Sucesso", "Horário inserido com sucesso! Bom Descanso!")
            else:
                # Nenhum registro encontrado, não faça nada
                messagebox.showinfo("Nenhum registro encontrado. Nenhum registro foi atualizado.")

        except Exception as e:
            messagebox.showinfo(f"Erro ao inserir ou atualizar registro de fim do Almoço: {str(e)}")

    data_hora_formatada = ""  # Defina a variável antes de usá-la
    label_data_hora = customtkinter.CTkLabel(
        janela_ponto,
        width=400,
        height=50,
        text=data_hora_formatada,
        font=("arial", 40),
        anchor="center",
        bg_color="#456320",
        corner_radius=10,
    )
    label_data_hora.grid(row=1, column=1, padx=5, pady=5, columnspan=560)






    ini_exp = customtkinter.CTkButton(
    janela_ponto, text= "Inicio do Expediente", command=inserir_ini_exp,
    width=130, height=50,border_width=2,)
    ini_exp.grid(row= 5, column= 1, padx=5, pady=5,)
    janela_ponto.after(1000,atualizar_hora)

    ini_alm = customtkinter.CTkButton(
    janela_ponto, text= "Inicio do Almoço", command=inserir_ini_alm,
    width=130, height=50,border_width=2,)
    ini_alm.grid(row= 5, column= 2, padx=5, pady=5,)

    fim_alm= customtkinter.CTkButton(
    janela_ponto, text= "Fim do Almoço", command=inserir_fim_alm,
    width=130, height=50,border_width=2,)
    fim_alm.grid(row= 5, column= 3, padx=5, pady=5,)

    fim_exp = customtkinter.CTkButton(
    janela_ponto, text= "Fim do Expediente", command=inserir_fim_exp,
    width=130, height=50,border_width=2,)
    fim_exp.grid(row= 5, column= 4, padx=5, pady=5,)


    janela_ponto.mainloop()

