import qrcode
from PIL import Image

# Defina o link que você deseja codificar no QR Code
link = "https://wa.me/%2B5519995155507?text=Ol%C3%A1%21%20Vi%20o%20anuncio%20da%20escola%20na%20Flex%2C%20gostaria%20de%20mais%20informa%C3%A7%C3%B5es%21"

# Crie o QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Adicione os dados ao QR Code
qr.add_data(link)
qr.make(fit=True)

# Crie uma imagem do QR Code em preto e branco
img = qr.make_image(fill_color="black", back_color="white")

# Carregue o logotipo colorido usando a biblioteca PIL (Pillow)
logo = Image.open("C:\\programa ponto\\qr\\logob.png")

# Redimensione o logotipo para que ele se ajuste ao QR Code
img_w, img_h = img.size
logo = logo.resize((img_w // 3, img_h // 3))

# Calcule a posição para o logotipo centralizado
x = (img_w - logo.width) // 2
y = (img_h - logo.height) // 2

# Cole o logotipo na imagem do QR Code
img.paste(logo, (x, y), logo)

# Salve a imagem do QR Code no diretório "C:\programa ponto\qr"
img.save("C:\\programa ponto\\qr\\qr_code_com_logo.png")
