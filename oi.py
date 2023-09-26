frase_substituicao = "como curar minha calvície ? por favor, me ajuda eu sou muito calvo e preciso de ajuda kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"
indice_substituicao = 0


def substituir_caractere(texto_digitado):
    global indice_substituicao

    if indice_substituicao < len(texto_digitado):
        caractere_substituido = frase_substituicao[indice_substituicao]
        texto_digitado = texto_digitado[:indice_substituicao] + caractere_substituido + texto_digitado[
                                                                                        indice_substituicao + 1:]
        indice_substituicao += 1
    return texto_digitado


print("Bem-vindo ao Chat Bot!")
print("Digite sua mensagem ou digite 'sair' para encerrar o chat.")

while True:
    entrada_usuario = input("Você: ")

    if entrada_usuario.lower() == "sair":
        print("Chat Bot: Chat encerrado.")
        break

    resposta_chatbot = substituir_caractere(entrada_usuario)
    print("Chat Bot:", resposta_chatbot)
