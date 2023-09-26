import urllib.parse

def criar_link_whatsapp(numero, mensagem):
    numero_whatsapp = urllib.parse.quote(numero)
    mensagem_codificada = urllib.parse.quote(mensagem)
    link = f"https://wa.me/{numero_whatsapp}?text={mensagem_codificada}"
    return link

# Exemplo de uso:
numero_destino = "+5519995155507"
mensagem = "Olá! Vi o anuncio da escola na Samsung, gostaria de mais informações!"
link_whatsapp = criar_link_whatsapp(numero_destino, mensagem)
print(link_whatsapp)